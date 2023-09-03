from prac_07.project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n" \
       "- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    options = ("l", "s", "d", "f", "a", "u", 'q')
    filename = "projects.txt"
    projects = []

    print(MENU)
    option = input(">>> ").lower()
    while option != options[-1]:
        if option == options[0]:
            projects = load_projects(filename)

        elif option == options[1]:
            save_projects(filename, projects)

        elif option == options[2]:
            display_projects(projects)

        elif option == options[3]:
            start_after_date = input("Show projects that start after date (dd/mm/yy):")
            filter_projects_by_date(projects, start_after_date)

        elif option == options[4]:
            new_project = add_new_project()
            projects.append(new_project)

        elif option == options[5]:
            update_project(projects)

        else:
            print("Invalid input.")
        print(MENU)
        option = input(">>> ").lower()
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        name = parts[0]
        start_date = parts[1]
        priority = int(parts[2])
        cost_estimate = float(parts[3])
        completion_percentage = int(parts[4])
        project = Project(name, start_date, priority, cost_estimate, completion_percentage)
        projects.append(project)
    in_file.close()
    return projects


def save_projects(filename, projects):
    out_file = open(filename, 'w')
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
    for project in projects:
        name = project.name
        start_date = project.start_date_str
        priority = project.priority
        cost_estimate = project.cost_estimate
        completion_percentage = project.completion_percentage
        print(f"{name}\t{start_date}\t{priority}\t{cost_estimate}\t{completion_percentage}", file=out_file)

    out_file.close()


def display_projects(projects):
    projects.sort()
    print("Incomplete projects:")
    for project in projects:
        if project.completion_percentage < 100:
            print(project)
    print("Completed projects:")
    for project in projects:
        if project.completion_percentage == 100:
            print(project)


def filter_projects_by_date(projects, start_after_date):
    dates = []
    for project in projects:
        if project.compare_date_with_input_date(start_after_date):
            dates.append(project.start_date)
    dates.sort()
    for date in dates:
        for project in projects:
            if date == project.start_date:
                print(project)


def add_new_project():
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    return project


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = int(input("Project choice: "))

    if 0 <= project_choice < len(projects):
        chosen_project = projects[project_choice]
        new_percentage = input("New Percentage: ")
        if new_percentage != "":
            chosen_project.completion_percentage = int(new_percentage)
        new_priority = input("New Priority: ")
        if new_priority != "":
            chosen_project.priority = int(new_priority)
    else:
        print("Invalid project choice.")


main()

