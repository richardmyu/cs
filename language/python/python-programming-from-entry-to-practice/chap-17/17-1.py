import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url_start = 'https://api.github.com/search/repositories?q=language:'
url_end = '&sort=stars'
languages = ['python', 'javascript', 'ruby', 'c', 'c++', 'c#', 'java', 'go', 'rust']


def get_language_info(language):
    try:
        r = requests.get(url_start + language + url_end)
        print(f'Status code of {language}: { r.status_code}')
        response_dict = r.json()
        repo_dicts = response_dict['items']
    except:
        pass
    else:
        return repo_dicts


def get_x_y(repo_dicts):
    if not repo_dicts:
        return None

    names, plot_dicts = [], []

    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': repo_dict['description'],
            'xlink': repo_dict['html_url'],
        }
        plot_dicts.append(plot_dict)

    return names, plot_dicts


def create_visual(language, names=[], plot_dicts=[]):
    my_style = LS('#333366', base_style=LCS)
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = f'Most-Starred {language.title()} Projects on Github'
    chart.x_labels = names
    chart.add('', plot_dicts)
    chart.render_to_file(f'{language}_repos_visual.svg')


for language in languages:
    repo_dicts = get_language_info(language)

    if repo_dicts:
        names, plot_dicts = get_x_y(repo_dicts)
        create_visual(language, names, plot_dicts)

with open(
    'most-starred-language-project-on-github.html', 'w', encoding='utf8'
) as html_file:
    html_file.write(
        '<html><head><title>不同语言的最受欢迎的项目</title><meta charset="utf-8"></head><body>\n'
    )

    for svg in [language + '_repos_visual.svg' for language in languages]:
        html_file.write(
            '    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(
                svg
            )
        )  # 1

    html_file.write('</body></html>')
