INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_SIGINT sigint)

FIND_PATH(
    SIGINT_INCLUDE_DIRS
    NAMES sigint/api.h
    HINTS $ENV{SIGINT_DIR}/include
        ${PC_SIGINT_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    SIGINT_LIBRARIES
    NAMES gnuradio-sigint
    HINTS $ENV{SIGINT_DIR}/lib
        ${PC_SIGINT_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(SIGINT DEFAULT_MSG SIGINT_LIBRARIES SIGINT_INCLUDE_DIRS)
MARK_AS_ADVANCED(SIGINT_LIBRARIES SIGINT_INCLUDE_DIRS)

