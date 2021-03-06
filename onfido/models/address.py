# coding: utf-8

"""
    Onfido API

    The Onfido API is used to submit check requests.

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Address(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, flat_number=None, building_number=None, building_name=None, street=None, sub_street=None, town=None, postcode=None, country=None, id=None, start_date=None, end_date=None, state=None):
        """
        Address - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'flat_number': 'str',
            'building_number': 'str',
            'building_name': 'str',
            'street': 'str',
            'sub_street': 'str',
            'town': 'str',
            'postcode': 'str',
            'country': 'str',
            'id': 'str',
            'start_date': 'date',
            'end_date': 'date',
            'state': 'str'
        }

        self.attribute_map = {
            'flat_number': 'flat_number',
            'building_number': 'building_number',
            'building_name': 'building_name',
            'street': 'street',
            'sub_street': 'sub_street',
            'town': 'town',
            'postcode': 'postcode',
            'country': 'country',
            'id': 'id',
            'start_date': 'start_date',
            'end_date': 'end_date',
            'state': 'state'
        }

        self._flat_number = flat_number
        self._building_number = building_number
        self._building_name = building_name
        self._street = street
        self._sub_street = sub_street
        self._town = town
        self._postcode = postcode
        self._country = country
        self._id = id
        self._start_date = start_date
        self._end_date = end_date
        self._state = state


    @property
    def flat_number(self):
        """
        Gets the flat_number of this Address.
        The flat number of this address

        :return: The flat_number of this Address.
        :rtype: str
        """
        return self._flat_number

    @flat_number.setter
    def flat_number(self, flat_number):
        """
        Sets the flat_number of this Address.
        The flat number of this address

        :param flat_number: The flat_number of this Address.
        :type: str
        """

        self._flat_number = flat_number

    @property
    def building_number(self):
        """
        Gets the building_number of this Address.
        The building number of this address

        :return: The building_number of this Address.
        :rtype: str
        """
        return self._building_number

    @building_number.setter
    def building_number(self, building_number):
        """
        Sets the building_number of this Address.
        The building number of this address

        :param building_number: The building_number of this Address.
        :type: str
        """

        self._building_number = building_number

    @property
    def building_name(self):
        """
        Gets the building_name of this Address.
        The building name of this address

        :return: The building_name of this Address.
        :rtype: str
        """
        return self._building_name

    @building_name.setter
    def building_name(self, building_name):
        """
        Sets the building_name of this Address.
        The building name of this address

        :param building_name: The building_name of this Address.
        :type: str
        """

        self._building_name = building_name

    @property
    def street(self):
        """
        Gets the street of this Address.
        The street of the applicant’s address

        :return: The street of this Address.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """
        Sets the street of this Address.
        The street of the applicant’s address

        :param street: The street of this Address.
        :type: str
        """

        self._street = street

    @property
    def sub_street(self):
        """
        Gets the sub_street of this Address.
        The sub-street of the applicant’s address

        :return: The sub_street of this Address.
        :rtype: str
        """
        return self._sub_street

    @sub_street.setter
    def sub_street(self, sub_street):
        """
        Sets the sub_street of this Address.
        The sub-street of the applicant’s address

        :param sub_street: The sub_street of this Address.
        :type: str
        """

        self._sub_street = sub_street

    @property
    def town(self):
        """
        Gets the town of this Address.
        The town of the applicant’s address

        :return: The town of this Address.
        :rtype: str
        """
        return self._town

    @town.setter
    def town(self, town):
        """
        Sets the town of this Address.
        The town of the applicant’s address

        :param town: The town of this Address.
        :type: str
        """

        self._town = town

    @property
    def postcode(self):
        """
        Gets the postcode of this Address.
        The postcode or ZIP of the applicant’s address

        :return: The postcode of this Address.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """
        Sets the postcode of this Address.
        The postcode or ZIP of the applicant’s address

        :param postcode: The postcode of this Address.
        :type: str
        """

        self._postcode = postcode

    @property
    def country(self):
        """
        Gets the country of this Address.
        The 3 character ISO country code of this address. For example, GBR is the country code for the United Kingdom

        :return: The country of this Address.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Address.
        The 3 character ISO country code of this address. For example, GBR is the country code for the United Kingdom

        :param country: The country of this Address.
        :type: str
        """

        self._country = country

    @property
    def id(self):
        """
        Gets the id of this Address.


        :return: The id of this Address.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Address.


        :param id: The id of this Address.
        :type: str
        """

        self._id = id

    @property
    def start_date(self):
        """
        Gets the start_date of this Address.
        The date the applicant started living at this address

        :return: The start_date of this Address.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this Address.
        The date the applicant started living at this address

        :param start_date: The start_date of this Address.
        :type: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this Address.
        The date the applicant left this address. If current residence, leave null

        :return: The end_date of this Address.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this Address.
        The date the applicant left this address. If current residence, leave null

        :param end_date: The end_date of this Address.
        :type: date
        """

        self._end_date = end_date

    @property
    def state(self):
        """
        Gets the state of this Address.
        The address state. US states must use the USPS abbreviation (see also ISO 3166-2:US), for example AK, CA, or TX.

        :return: The state of this Address.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Address.
        The address state. US states must use the USPS abbreviation (see also ISO 3166-2:US), for example AK, CA, or TX.

        :param state: The state of this Address.
        :type: str
        """

        self._state = state

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
