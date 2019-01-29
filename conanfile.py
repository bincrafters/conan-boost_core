#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostCoreConan(base.BoostBaseConan):
    name = "boost_core"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_core"
    lib_short_names = ["core"]
    header_only_libs = ["core"]
    b2_requires = [
        "boost_assert",
        "boost_config"
    ]
