from django.conf.urls import patterns, url

from scrum.views import (CreateBZUrlView, CreateProjectView, CreateSprintView,
                         CreateTeamView, DeleteBZUlrView, EditProjectView,
                         EditSprintView, ListProjectsView, ListTeamsView,
                         ManageSprintBugsView, ProjectView, RedirectOldURLsView,
                         SprintView, TeamView)


urlpatterns = patterns('',
    url(r'^p/$', ListProjectsView.as_view(), name='scrum_projects_list'),
    url(r'^t/$', ListTeamsView.as_view(), name='scrum_teams_list'),
    url(r'^p/new/$', CreateProjectView.as_view(), name='scrum_project_new'),
    url(r'^t/new/$', CreateTeamView.as_view(), name='scrum_team_new'),
    url(r'^p/url/(?P<pk>\d+)/delete/$', DeleteBZUlrView.as_view(),
        name='scrum_url_delete'),
    url(r'^p/(?P<slug>[-\w]+)/$', ProjectView.as_view(), name='scrum_project'),
    url(r'^t/(?P<slug>[-\w]+)/$', TeamView.as_view(), name='scrum_team'),
    url(r'^t/(?P<slug>[-\w]+)/new/$', CreateSprintView.as_view(),
        name='scrum_sprint_new'),
    url(r'^p/(?P<slug>[-\w]+)/edit/$', EditProjectView.as_view(),
        name='scrum_project_edit'),
    url(r'^p/(?P<slug>[-\w]+)/urls/$', CreateBZUrlView.as_view(),
        name='scrum_project_urls'),
    url(r'^t/(?P<slug>[-\w]+)/(?P<sslug>[-\w\.]+)/$', SprintView.as_view(),
        name='scrum_sprint'),
    url(r'^t/(?P<slug>[-\w]+)/(?P<sslug>[-\w\.]+)/edit/$',
        EditSprintView.as_view(), name='scrum_sprint_edit'),
    url(r'^t/(?P<slug>[-\w]+)/(?P<sslug>[-\w\.]+)/bugs/$',
        ManageSprintBugsView.as_view(), name='scrum_sprint_bugs'),
    url(r'^projects/(?P<path>.*)', RedirectOldURLsView.as_view()),
)
