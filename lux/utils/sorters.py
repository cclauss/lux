#  Copyright 2019-2020 The Lux Authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


class Sorter:

    @staticmethod
    def interestingness():
        return lambda x: x.score

    @staticmethod
    def title():
        return lambda x: x.title

    @staticmethod
    def x_alpha():
        return lambda x: x.get_attr_by_channel("x")[0].attribute

    @staticmethod
    def y_alpha():
        return lambda x: x.get_attr_by_channel("y")[0].attribute