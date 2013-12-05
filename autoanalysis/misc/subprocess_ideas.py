import sys
from tempfile import TemporaryFile
from subprocess import Popen, CalledProcessError, PIPE
import threading

def _writeStreamToFile(stream, fname):
  '''Simple function used internally to pipe a stream to a file.'''
  for data in stream:
    fname.write(data)

def callSubprocess(cmd, shell=False, **kwargs):

  '''Generic wrapper around subprocess calls with handling of failed
  calls. This function starts threads to read stdout and stderr from
  the child process. In so doing it avoids deadlocking issues when
  reading large quantities of data from the stdout of the child
  process.'''

  # Credit to the maintainer of python-gnupg, Vinay Sajip, for the
  # basic design of this function.

  # We have **kwargs here mainly so we can support shell=True.
  kid = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=shell, **kwargs)

  stdoutfd = TemporaryFile()
  stderrfd = TemporaryFile()

  # We store streams in our own variables to avoid unexpected pitfalls
  # in how the subprocess object manages its attributes. This is
  # probably overly paranoid.
  stderr = kid.stderr
  err_read = threading.Thread(target=_writeStreamToFile,
                              args=(stderr, stderrfd))
  err_read.setDaemon(True)
  err_read.start()

  stdout = kid.stdout
  out_read = threading.Thread(target=_writeStreamToFile,
                              args=(stdout, stdoutfd))
  out_read.setDaemon(True)
  out_read.start()

  out_read.join()
  err_read.join()
  retcode = kid.wait()
  stderr.close()
  stdout.close()
  stdoutfd.seek(0, 0)

  if retcode != 0:
    stderrfd.seek(0, 0)
    sys.stderr.write("\nSubprocess STDOUT:\n")
    for line in stdoutfd:
      sys.stderr.write("%s\n" % (line,))
    sys.stderr.write("\nSubprocess STDERR:\n")
    for line in stderrfd:
      sys.stderr.write("%s\n" % (line,))
    if type(cmd) == list:
      cmd = " ".join(cmd)
    raise CalledProcessError(kid.returncode, cmd)
  return stdoutfd


def background(fun, *args, **kwargs):
  """Run a function, but return a Future object instead of blocking.

Instead of blocking, it starts the function in a separate thread,
and returns an object which lets the user choose when to wait for
the function by calling its wait() method. wait() blocks its
current thread until the function returns, then wait returns the
value returned by the function.

f = background(sqrt, 0)
a = f.wait()

is exactly equivalent to

a = sqrt(0)

except that in the first case, sqrt is run in a separate thread.

The argument list after *fun* is exactly what you would pass to
*fun* if you were calling it directly, including keyword
arguments.
"""
  class Future(object):
      def __init__(self):
          self.return_value = None

      def wait(self):
          v.wait()
          return self.return_value
  future = Future()
  v = threading.Event()
  def g():
      future.return_value = fun(*args, **kwargs)
      v.set()
  a = threading.Thread(target=g)
  a.start()
  return(future)

