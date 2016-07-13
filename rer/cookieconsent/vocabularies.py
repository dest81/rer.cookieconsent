# -*- coding: utf-8 -*-

from plone import api
from operator import itemgetter
from plone.app.vocabularies.language import AvailableContentLanguageVocabulary
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class SupportedContentLanguageVocabulary(AvailableContentLanguageVocabulary):

    def __call__(self, context):
        items = []
        ltool = api.portal.get_tool('portal_languages')
        if ltool is not None:
            items = ltool.listSupportedLanguages()
            items.sort(key=itemgetter(1))
            items = [SimpleTerm(i[0].decode('utf-8'), i[0].decode('utf-8'), i[1].decode('utf-8')) for i in items]
        return SimpleVocabulary(items)


SupportedContentLanguageVocabularyFactory = SupportedContentLanguageVocabulary()