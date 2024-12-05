from flask import Blueprint, render_template, redirect, url_for, request, session

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('views.home'))  # أو url_for('auth.login') بناءً على متطلباتك

@auth.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')


def test_concurrent_sign_up_requests(self):
    with self.app.app_context():
        from concurrent.futures import ThreadPoolExecutor, as_completed
        response = self.client.get('/sign-up')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<html', response.data)
        self.assertIn(b'</html>', response.data)
    
        def make_request():
            return self.client.get('/sign-up')
        
        num_requests = 10
        with ThreadPoolExecutor(max_workers=num_requests) as executor:
            futures = [executor.submit(make_request) for _ in range(num_requests)]
            responses = [future.result() for future in as_completed(futures)]
        
        for response in responses:
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'sign-up.html', response.data)