
class CONSTANTS:
    DEBUG = True
    LOGFILE = 'resources/pwanalysis.log'

    # Input File constants
    BLOCK_SIZE = 1000
    DELIM = ":"


class FUNCTIONS:

    FREQ_ANALYSIS = 'Frequency Analysis'
    USER_PASS_COMP = 'Username Password Comparison'

    USER_PASS_MODULES = (
        FREQ_ANALYSIS,
        USER_PASS_COMP,
    )

    PASSWORD_MODULES = (
        FREQ_ANALYSIS,
    )

    MODULES = {
        FREQ_ANALYSIS: 'analytics.frequencies.FreqAnalyzer',
        USER_PASS_COMP: 'analytics.comparisons.ComparisonAnalyzer',
    }


class MODES:
    MODE_USERPASS = 'userpass'
    MODE_PASSWORD = 'password'

    ALL_MODES = (
        MODE_USERPASS,
        MODE_PASSWORD,
    )
