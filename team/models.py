from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


SERVICES = (
	('Trello', 'Trello'),
	('Github', 'Github'),
	('Bitbucket', 'Bitbucket'),
	('Slack', 'Slack'),
	('Google Apps', 'Google Apps'),
	('Jira', 'Jira'),
	# ('Confluence', 'Confluence'),
	('HipChat', 'HipChat'),
)

class Service(models.Model):
	"""
	Service models.Model
	named for Github
	needs to be modified
	"""
	name = models.CharField(choices=SERVICES, max_length=50)
	# password-bitbucket, team_token-slack, password-jira, token in hipchat, token in trello
	token = models.CharField(max_length=200, null=True, blank=True)
	# groupslug-bitbucket, sitename-jira, key in trello
	org_name = models.CharField(max_length=200, null=True, blank=True)
	# team short name in trello
	team_name = models.CharField(max_length=200, null=True, blank=True)
	# in trello
	team_id = models.CharField(max_length=200, null=True, blank=True)
	is_active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name


class Account(models.Model):
	"""
	Account level class
	"""
	name = models.CharField(max_length=50)
	team_limit = models.IntegerField(default=0)
	budget = models.IntegerField(default=0)
	description = models.TextField(null=True, blank=True)
	stripe_id = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name
		
		
class TeamUser(AbstractUser):
	"""
	Team user class, it could be team owner, too.
	"""
	account = models.ForeignKey(Account, related_name="account", null=True, blank=True)
	is_temp = models.BooleanField(default=False)
	exp_date = models.DateField(null=True, blank=True)
	last4_card_num = models.CharField(max_length=4, null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	customer_id = models.CharField(max_length=50, null=True, blank=True)
	subscription_id = models.CharField(max_length=50, null=True, blank=True)

	def __unicode__(self):
		return self.username


class Team(models.Model):
	"""
	team class
	"""
	name = models.CharField(max_length=50)
	owner = models.ForeignKey(TeamUser, related_name="owner")
	member = models.ManyToManyField(TeamUser, related_name='team_member', blank=True)
	service = models.ManyToManyField(Service, related_name='team_service', blank=True)
	is_active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name
