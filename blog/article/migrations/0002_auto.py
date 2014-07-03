# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field category on 'Article'
        m2m_table_name = db.shorten_name(u'article_article_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm[u'article.article'], null=False)),
            ('category', models.ForeignKey(orm[u'category.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['article_id', 'category_id'])


    def backwards(self, orm):
        # Removing M2M table for field category on 'Article'
        db.delete_table(db.shorten_name(u'article_article_category'))


    models = {
        u'article.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['category.Category']", 'symmetrical': 'False'}),
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
        },
        u'category.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['article']