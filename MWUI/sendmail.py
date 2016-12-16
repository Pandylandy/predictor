#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
#
#  Copyright 2016 Ramil Nugmanov <stsouko@live.ru>
#  This file is part of predictor.
#
#  predictor 
#  is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
from redis import Redis, ConnectionError
from rq import Queue

from flask_misaka import markdown
from flask import render_template
from .config import LAB_NAME, SMTP_MAIL


def send_mail(message, to_mail, to_name=None, from_name=None, subject=None, banner=None, title=None,
              reply_name=None, reply_mail=None):

    #tasks = Redis(host=host, port=port, password=password)

    email = dict(html=render_template('email.html', body=markdown(message), banner=banner, title=title),
                 message=message, subject=subject or "", mail_from='%s <%s>' % (from_name or LAB_NAME, SMTP_MAIL),
                 mail_to='%s <%s>' % (to_name, to_mail) if to_name else to_mail,
                 reply_to='%s <%s>' % (reply_name, reply_mail) if reply_name else reply_mail)
