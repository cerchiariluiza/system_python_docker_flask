from flask import url_for

def test_home(create_user,client,captured_templates):
    resp = client.get(url_for('core.home'),follow_redirects=True)
    template, context = captured_templates[0]
    assert resp.status_code == 200