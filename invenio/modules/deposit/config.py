# -*- coding: utf-8 -*-
## This file is part of Invenio.
## Copyright (C) 2014 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

DEPOSIT_TYPES = [
    'invenio.modules.deposit.workflows.article_metadata.Article',
    'invenio.modules.deposit.workflows.photo_metadata.Photo',
    'invenio.modules.deposit.workflows.poetry_metadata.Poetry',
    'invenio.modules.deposit.workflows.preprint_metadata.Preprint',
    'invenio.modules.deposit.workflows.thesis_metadata.Thesis',
]
"""
List of DepositionType import strings

Import string must be to the actual subclass of DepositionType, e.g.::

    invenio.modules.deposit.workflows.article_workflow:Article

Also, each DepositionType is a workflow, so the workflow module must also
be able to load the module it, which usually means that your
DepositionType must be located in a package called ''workflows'' in an Invenio
module, e.g.::

    mysite/modules/myappmodule/workflows/mydep.py

Then your config will look like something like this::

    PACKAGES = [
        "mysite.modules.myappmodule",
        # ...
    ]

    DEPOSIT_TYPES = [
        # ...
        "mysite.modules.myappmodule.workflows.mydep:MyDepTypeSubclass"
    ]

"""

DEPOSIT_DEFAULT_TYPE = None
""" Import string of default deposition type """
