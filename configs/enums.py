from enum import Enum


class LogLevels(str, Enum):
    info = "INFO"
    warn = "WARN"
    error = "ERROR"
    debug = "DEBUG"


class Environment(str, Enum):
    local = "LOCAL"
    staging = "STAGING"
    production = "PRODUCTION"
