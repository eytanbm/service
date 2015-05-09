# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table('location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('room_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('other_location', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
        ))
        db.send_create_signal('content', ['Location'])

        # Adding model 'Guest'
        db.create_table('guest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('room', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('content', ['Guest'])

        # Adding model 'Content'
        db.create_table('content', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ticket', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='content', unique=True, null=True, to=orm['service_calls.Ticket'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='content', null=True, to=orm['content.Location'])),
            ('guest', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='content', null=True, to=orm['content.Guest'])),
            ('fault', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='content', null=True, to=orm['service_calls.Fault'])),
        ))
        db.send_create_signal('content', ['Content'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table('location')

        # Deleting model 'Guest'
        db.delete_table('guest')

        # Deleting model 'Content'
        db.delete_table('content')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'content.content': {
            'Meta': {'object_name': 'Content', 'db_table': "'content'"},
            'fault': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content'", 'null': 'True', 'to': "orm['service_calls.Fault']"}),
            'guest': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content'", 'null': 'True', 'to': "orm['content.Guest']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content'", 'null': 'True', 'to': "orm['content.Location']"}),
            'ticket': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'content'", 'unique': 'True', 'null': 'True', 'to': "orm['service_calls.Ticket']"})
        },
        'content.guest': {
            'Meta': {'object_name': 'Guest', 'db_table': "'guest'"},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'room': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'content.location': {
            'Meta': {'object_name': 'Location', 'db_table': "'location'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other_location': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'room_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'service_calls.fault': {
            'Meta': {'object_name': 'Fault', 'db_table': "'fault'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        },
        'service_calls.ticket': {
            'Meta': {'object_name': 'Ticket', 'db_table': "'ticket'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tickets'", 'null': 'True', 'to': "orm['service_calls.TicketRole']"}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'source': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'service_calls.ticketrole': {
            'Meta': {'unique_together': "(('user', 'role'),)", 'object_name': 'TicketRole', 'db_table': "'ticket_role'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ticket_roles'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['content']