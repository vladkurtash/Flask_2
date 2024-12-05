from flask import Flask, render_template, Blueprint

def create_app(test_config=None):
    app = Flask(__name__, 
        template_folder='flaskr/templates',
        static_folder='flaskr/static',
        static_url_path=''
    )
    
    # Create a main blueprint for our basic pages
    main = Blueprint('main', __name__)
    
    @main.route('/')
    def index():
        return render_template('blog/index.html')

    @main.route('/about')
    def about():
        return render_template('about.html')

    @main.route('/contacts')
    def contacts():
        return render_template('contacts.html')

    @main.route('/services')
    def services():
        return render_template('services.html')

    # Register the main blueprint
    app.register_blueprint(main)

    # Register other blueprints
    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=False, port=5000)