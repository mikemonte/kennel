# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pet'
        db.create_table(u'pet_pet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('salt', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('short_salt', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('food', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('emergency', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=2, null=True, blank=True)),
            ('care', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('walk', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'pet', ['Pet'])

        # Adding model 'Owner'
        db.create_table(u'pet_owner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('salt', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('short_salt', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'pet', ['Owner'])

        # Adding M2M table for field pets on 'Owner'
        m2m_table_name = db.shorten_name(u'pet_owner_pets')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('owner', models.ForeignKey(orm[u'pet.owner'], null=False)),
            ('pet', models.ForeignKey(orm[u'pet.pet'], null=False))
        ))
        db.create_unique(m2m_table_name, ['owner_id', 'pet_id'])

        # Adding model 'Kennel'
        db.create_table(u'pet_kennel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('salt', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('short_salt', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('manager', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('kennel_name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'pet', ['Kennel'])

        # Adding M2M table for field owners on 'Kennel'
        m2m_table_name = db.shorten_name(u'pet_kennel_owners')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('kennel', models.ForeignKey(orm[u'pet.kennel'], null=False)),
            ('owner', models.ForeignKey(orm[u'pet.owner'], null=False))
        ))
        db.create_unique(m2m_table_name, ['kennel_id', 'owner_id'])


    def backwards(self, orm):
        # Deleting model 'Pet'
        db.delete_table(u'pet_pet')

        # Deleting model 'Owner'
        db.delete_table(u'pet_owner')

        # Removing M2M table for field pets on 'Owner'
        db.delete_table(db.shorten_name(u'pet_owner_pets'))

        # Deleting model 'Kennel'
        db.delete_table(u'pet_kennel')

        # Removing M2M table for field owners on 'Kennel'
        db.delete_table(db.shorten_name(u'pet_kennel_owners'))


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pet.kennel': {
            'Meta': {'object_name': 'Kennel'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'kennel_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pet.Owner']", 'symmetrical': 'False'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'salt': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'short_salt': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'pet.owner': {
            'Meta': {'object_name': 'Owner'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'pets': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pet.Pet']", 'symmetrical': 'False'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'salt': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'short_salt': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'pet.pet': {
            'Meta': {'ordering': "['name']", 'object_name': 'Pet'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'care': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'emergency': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'food': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'salt': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'short_salt': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'walk': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'})
        }
    }

    complete_apps = ['pet']