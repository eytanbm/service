# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TicketRole'
        db.create_table('ticket_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ticket_roles', to=orm['auth.User'])),
            ('role', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('service_calls', ['TicketRole'])

        # Adding unique constraint on 'TicketRole', fields ['user', 'role']
        db.create_unique('ticket_role', ['user_id', 'role'])

        # Adding model 'Ticket'
        db.create_table('ticket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('source', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='tickets', null=True, to=orm['service_calls.TicketRole'])),
        ))
        db.send_create_signal('service_calls', ['Ticket'])

        # Adding model 'TicketEvent'
        db.create_table('ticket_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ticket', self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', to=orm['service_calls.Ticket'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 5, 3, 0, 0))),
            ('by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('service_calls', ['TicketEvent'])

        # Adding model 'TicketAttrChange'
        db.create_table('ticket_event_attribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(related_name='atrributes', to=orm['service_calls.TicketEvent'])),
            ('attr', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal('service_calls', ['TicketAttrChange'])


    def backwards(self, orm):
        # Removing unique constraint on 'TicketRole', fields ['user', 'role']
        db.delete_unique('ticket_role', ['user_id', 'role'])

        # Deleting model 'TicketRole'
        db.delete_table('ticket_role')

        # Deleting model 'Ticket'
        db.delete_table('ticket')

        # Deleting model 'TicketEvent'
        db.delete_table('ticket_event')

        # Deleting model 'TicketAttrChange'
        db.delete_table('ticket_event_attribute')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        'service_calls.ticketattrchange': {
            'Meta': {'object_name': 'TicketAttrChange', 'db_table': "'ticket_event_attribute'"},
            'attr': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'atrributes'", 'to': "orm['service_calls.TicketEvent']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        'service_calls.ticketevent': {
            'Meta': {'object_name': 'TicketEvent', 'db_table': "'ticket_event'"},
            'by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ticket': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': "orm['service_calls.Ticket']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 5, 3, 0, 0)'})
        },
        'service_calls.ticketrole': {
            'Meta': {'unique_together': "(('user', 'role'),)", 'object_name': 'TicketRole', 'db_table': "'ticket_role'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ticket_roles'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['service_calls']