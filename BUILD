# Top level package of the phd repo.

config_setting(
    name = "darwin",
    values = {"cpu": "darwin"},
    visibility = ["//visibility:public"],
)

filegroup(
    name = "config",
    srcs = ["config.pbtxt"],
    visibility = ["//config:__subpackages__"],
)

filegroup(
    name = "configure_py",
    srcs = ["configure"],
)
