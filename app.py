# https://towardsdatascience.com/how-to-debug-flask-applications-in-vs-code-c65c9bdbef21

from api import OpenData, MLStripper
from flask import Flask, render_template, request

app = Flask(__name__)

opendata  = OpenData()

@app.template_filter('raw_html')
def strip_tags(html):
    s = MLStripper()
    try:
        s.feed(html)
        return s.get_data()
    except:
        return 

def list_attachments(attachment_pointer):
    html = []
    try:
        attachments_lookup = opendata.get_attachments(attachment_pointer['href'])
        for a in attachments_lookup:
            try:
                html.append(f'''<li><a href="{a['href']}">{a['href']}</a></li>''')
            except:
                pass
    except:
        pass
    return f"<ul> { [x for x in html] } </ul>"
    # return html


app.jinja_env.globals.update(list_attachments=list_attachments)


@app.route("/")
def hello():

    results = opendata.get_last_100()

    # # optional processing before we pass it into the template for display
    # for result in results:
    #     pass

    return render_template('index.html', results=results)

if __name__ == "__main__":
    app.run(host='0.0.0.0')


