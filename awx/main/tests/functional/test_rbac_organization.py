import pytest

from awx.main.access import OrganizationAccess

@pytest.mark.django_db
def test_organization_migration_admin(organization, permissions, user):
    u = user('admin', True)
    organization.admins.add(u)

    migrated_users = organization.migrate_to_rbac()
    assert len(migrated_users) == 1
    assert organization.accessible_by(u, permissions['admin']) == True

@pytest.mark.django_db
def test_organization_migration_user(organization, permissions, user):
    u = user('user', False)
    organization.users.add(u)

    migrated_users = organization.migrate_to_rbac()
    assert len(migrated_users) == 1
    assert organization.accessible_by(u, permissions['auditor']) == True

@pytest.mark.django_db
def test_organization_access_superuser(organization, user):
    access = OrganizationAccess(user('admin', True))
    assert access.can_change(organization, None) == True

@pytest.mark.django_db
def test_organization_access_admin(organization, user):
    u = user('admin', False)
    organization.admins.add(u)

    access = OrganizationAccess(u)
    assert access.can_change(organization, None) == True

@pytest.mark.django_db
def test_organization_access_user(organization, user):
    access = OrganizationAccess(user('user', False))
    assert access.can_change(organization, None) == False
