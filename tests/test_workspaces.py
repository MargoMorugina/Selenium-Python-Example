import allure
import pytest
from assertpy import assert_that

from helper_enums.status_enum import StatusEnum
from pages.about_page import AboutPage
from pages.login_page import LoginPage
from pages.project_edit_page import ProjectEditPage
from pages.project_type_page import ProjectTypePage
from pages.projects_page import ProjectsPage
from pages.templates_page import TemplatesPage
from utils.json_parser import JsonParser


# performs login operation
def login(prep_properties):
    config = prep_properties
    username = config.config_section_dict("Base Url")["username"]
    password = config.config_section_dict("Base Url")["password"]
    about_page = AboutPage()
    login_page = LoginPage()
    about_page.click_login_link()
    login_page.login(username, password)


@allure.epic("Workspaces")
@allure.story("WorkSpaces Creation and Editing Functionality")
@allure.severity(allure.severity_level.NORMAL)
class TestWorkspaces:
    _JSON_FILE_NAME = "workspaces_test_data.json"

    @allure.description("Create new Workspace test")
    @allure.title("Create new workspace test")
    @pytest.mark.run(order=1)
    def test_create_new_workspace(self, create_driver, prep_properties):
        login(prep_properties)
        json_reader = JsonParser(self._JSON_FILE_NAME)
        projects_page = ProjectsPage()
        before = projects_page.get_workspaces_number()
        projects_page.create_workspace(json_reader.read_from_json()["workspace_test"]["workspace_name"])
        after = projects_page.get_workspaces_number()
        assert_that(after).is_greater_than(before)

    @allure.description("Rename an existing workspace test")
    @allure.title("Rename an existing workspace test")
    @pytest.mark.run(order=2)
    def test_rename_workspace(self, create_driver, prep_properties):
        login(prep_properties)
        json_reader = JsonParser(self._JSON_FILE_NAME)
        projects_page = ProjectsPage()
        projects_page.rename_workspace(json_reader.read_from_json()["workspace_test"]["workspace_name"],
                                       json_reader.read_from_json()["workspace_test"]["new_workspace_name"])
        expected_status = projects_page.is_workspace_found(
            json_reader.read_from_json()["workspace_test"]["new_workspace_name"])
        assert_that(expected_status).is_true()

    @allure.description("Delete an existing workspace test")
    @allure.title("Delete existing workspace test")
    @pytest.mark.run(order=3)
    def test_delete_workspace(self, create_driver, prep_properties):
        login(prep_properties)
        projects_page = ProjectsPage()
        before = projects_page.get_workspaces_number()
        projects_page.delete_workspace()
        after = projects_page.get_workspaces_number()
        assert_that(after).is_less_than(before)

    @allure.description(
        "Compare between the actual number of projects seen on page and the number shown in workspaces block")
    @allure.title("Number of projects displayed in page test")
    @pytest.mark.run(order=4)
    def test_number_of_existing_projects(self, create_driver, prep_properties):
        login(prep_properties)
        projects_page = ProjectsPage()
        number_of_displayed_projects = projects_page.get_projects_number_in_page()
        number_of_projects_in_workspace = projects_page.get_projects_number_from_workspace()
        assert_that(number_of_displayed_projects).is_equal_to(number_of_projects_in_workspace)

    @allure.description("Selecting and adding a project to workspace")
    @allure.title("Add project to workspace test")
    @pytest.mark.run(order=5)
    def test_add_project_to_workspace(self, create_driver, prep_properties):
        login(prep_properties)
        json_reader = JsonParser(self._JSON_FILE_NAME)
        projects_page = ProjectsPage()
        project_type_page = ProjectTypePage()
        templates_page = TemplatesPage()
        project_edit_page = ProjectEditPage()
        before = projects_page.get_projects_number_in_page()
        projects_page.create_new_project()
        project_type_page.select_project(json_reader.read_from_json()["workspace_test"]["project_type"])
        templates_page.choose_template(json_reader.read_from_json()["workspace_test"]["template_type"])
        project_edit_page.edit_project_prep(json_reader.read_from_json()["workspace_test"]["project_name"],
                                            json_reader.read_from_json()["workspace_test"]["final_slide"])
        project_edit_page.click_save_and_exit()
        after = projects_page.get_projects_number_in_page()
        assert_that(before + 1).is_equal_to(after)

    @allure.description("Search for an existing project")
    @allure.title("Search for existing project test")
    @pytest.mark.run(order=6)
    def test_search_project(self, create_driver, prep_properties):
        login(prep_properties)
        projects_page = ProjectsPage()
        json_reader = JsonParser(self._JSON_FILE_NAME)
        projects_page.search_project(json_reader.read_from_json()["workspace_test"]["project_name"])
        expected_status = projects_page.is_project_found(json_reader.read_from_json()["workspace_test"]["project_name"])
        assert_that(expected_status).is_true()

    @allure.description("Search for a non existing project")
    @allure.title("Search for non existing project test")
    @pytest.mark.run(order=7)
    def test_search_for_non_existing_project(self, create_driver, prep_properties):
        login(prep_properties)
        json_reader = JsonParser(self._JSON_FILE_NAME)
        projects_page = ProjectsPage()
        projects_page.search_project(json_reader.read_from_json()["workspace_test"]["non_existing_project"])
        expected_not_found_msg = json_reader.read_from_json()["workspace_test"]["no_project_found_msg"]
        assert_that(expected_not_found_msg).is_equal_to(projects_page.get_no_project_found_msg())

    @allure.description("Cancel project deletion")
    @allure.title("Cancel a project deletion test")
    @pytest.mark.run(order=8)
    def test_cancel_project_deletion(self, create_driver, prep_properties):
        login(prep_properties)
        json_reader = JsonParser(self._JSON_FILE_NAME)
        projects_page = ProjectsPage()
        before = projects_page.get_projects_number_in_page()
        projects_page.delete_project(json_reader.read_from_json()["workspace_test"]["project_name"],
                                     StatusEnum.CANCEL.value)
        after = projects_page.get_projects_number_in_page()
        assert_that(before).is_equal_to(after)

    @allure.description("Deleting an existing project from workspace")
    @allure.title("Delete existing project test")
    @pytest.mark.run(order=9)
    def test_delete_project(self, create_driver, prep_properties):
        login(prep_properties)
        json_reader = JsonParser(self._JSON_FILE_NAME)
        projects_page = ProjectsPage()
        before = projects_page.get_projects_number_in_page()
        projects_page.delete_project(json_reader.read_from_json()["workspace_test"]["project_name"])
        after = projects_page.get_projects_number_in_page()
        assert_that(before).is_equal_to(after + 1)
