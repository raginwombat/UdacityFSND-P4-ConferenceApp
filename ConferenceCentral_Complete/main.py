#!/usr/bin/env python

"""
main.py -- Udacity conference server-side Python App Engine
    HTTP controller handlers for memcache & task queue access

$Id$

created by wesc on 2014 may 24

"""

__author__ = 'wesc+api@google.com (Wesley Chun)'

import webapp2
import logging
from google.appengine.api import app_identity
from google.appengine.api import mail
from conference import ConferenceApi
from models import Session
from google.appengine.api import taskqueue

class SetAnnouncementHandler(webapp2.RequestHandler):
    def get(self):
        """Set Announcement in Memcache."""
        ConferenceApi._cacheAnnouncement()
        self.response.set_status(204)


class SendConfirmationEmailHandlerConference(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Conference creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % (
                app_identity.get_application_id()),     # from
            self.request.get('email'),                  # to
            'You created a new Conference!',            # subj
            'Hi, you have created a following '         # body
            'conference:\r\n\r\n%s' % self.request.get(
                'conferenceInfo')
        )

class SendConfirmationEmailHandlerSession(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Session creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % (
                app_identity.get_application_id()),     # from
            self.request.get('email'),                  # to
            'You created a new Session!',            # subj
            'Hi, you have created a following '         # body
            'session:\r\n\r\n%s' % self.request.get(
                'sessionInfo')
        )

class SetFeaturedSpeakerHandler(webapp2.RequestHandler):
    def post(self):
        """Set featured speaker list in Memcache"""
        logging.info("Hit features speaker handler")
        wsck = self.request.get('wsck')
        s_key = self.request.get('s_key')
        #speakers = self.request.get('speakers')

        logging.info("wsck : %s", wsck)
        #logging.info("speakers : %s", speakers)

        
        ConferenceApi._cacheFeaturedSpeakers(wsck, s_key)
        """"Return Response"""
        logging.info('exitied handler')
        self.response.set_status(204)


app = webapp2.WSGIApplication([
    ('/crons/set_announcement', SetAnnouncementHandler),
    ('/tasks/send_confirmation_email_conference', SendConfirmationEmailHandlerConference),
    ('/tasks/send_confirmation_email_session', SendConfirmationEmailHandlerSession),
    ('/tasks/featured_speaker_check',SetFeaturedSpeakerHandler )
], debug=True)
