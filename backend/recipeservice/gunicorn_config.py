import multiprocessing

# ✅ Bind to all available network interfaces (IPv4 & IPv6)
bind = "0.0.0.0:5000"

# ✅ Number of worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# ✅ Enable threaded workers for handling multiple requests
threads = 2

# ✅ Use an async worker class for better concurrency
worker_class = "gthread"

# ✅ Set request timeout to prevent long-running requests
timeout = 120

# ✅ Enable access logging
accesslog = "-"

# ✅ Enable error logging
errorlog = "-"

# ✅ Set log level (options: debug, info, warning, error, critical)
loglevel = "info"
