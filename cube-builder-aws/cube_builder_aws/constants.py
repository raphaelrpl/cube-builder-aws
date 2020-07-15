#
#
# This file is part of Python Module for Cube Builder AWS.
# Copyright (C) 2019-2020 INPE.
#
# Cube Builder AWS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Define the Brazil Data Cube Builder constants."""


CLEAR_OBSERVATION_NAME = 'CLEAROB'

CLEAR_OBSERVATION_ATTRIBUTES = dict(
    name=CLEAR_OBSERVATION_NAME,
    description='Clear Observation Count.',
    data_type='uint8',
    min=0,
    max=255,
    fill=0,
    scale=1,
    common_name='ClearOb',
)

TOTAL_OBSERVATION_NAME = 'TOTALOB'

TOTAL_OBSERVATION_ATTRIBUTES = dict(
    name=TOTAL_OBSERVATION_NAME,
    description='Total Observation Count',
    data_type='uint8',
    min=0,
    max=255,
    fill=0,
    scale=1,
    common_name='TotalOb',
)

PROVENANCE_NAME = 'PROVENANCE'

PROVENANCE_ATTRIBUTES = dict(
    name=PROVENANCE_NAME,
    description='Provenance value Day of Year',
    data_type='int16',
    min=1,
    max=366,
    fill=-1,
    scale=1,
    common_name='Provenance',
)