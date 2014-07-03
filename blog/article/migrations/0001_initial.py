# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'article_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('body', self.gf('tinymce.models.HTMLField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('likes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'article', ['Article'])

        # Adding model 'Comment'
        db.create_table(u'article_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('writer', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['article.Article'])),
        ))
        db.send_create_signal(u'article', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'article_article')

        # Deleting model 'Comment'
        db.delete_table(u'article_comment')


    models = {
        u'article.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'article.comment': {
            'Meta': {'ordering': "('date',)", 'object_name': 'Comment'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article.Article']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'writer': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['article']