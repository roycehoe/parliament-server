class HansardAPICallException(Exception):
    pass


class NoParliamentDateFileException(Exception):
    pass


class CorruptedParliamentDateFileReadException(Exception):
    pass


class CorruptedParliamentDateFileWriteException(Exception):
    pass


class EmptyParliamentDateFileException(Exception):
    pass


class NoParliamentDataFileException(Exception):
    pass


class CorruptedParliamentDataFileReadException(Exception):
    pass


class CorruptedParliamentDataFileWriteException(Exception):
    pass


class EmptyParliamentDataFileException(Exception):
    pass


class NoRedisDataException(Exception):
    pass


class CorruptedRedisDataException(Exception):
    pass


class DateRangeException(Exception):
    pass
