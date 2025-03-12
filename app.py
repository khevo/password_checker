from flask import Flask, render_template, request, jsonify
import random
import string
import hashlib
import requests

app = Flask(__name__)

def generate_strong_password():
    """Generate a strong password between 8-12 characters"""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%&?"
    
    length = random.randint(8, 12)
    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    while len(password) < length:
        password.append(random.choice(lowercase + uppercase + digits + symbols))
    
    random.shuffle(password)
    return ''.join(password)

def check_password_online(password):
    """Check if password has been exposed in data breaches"""
    try:
        sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix = sha1_password[:5]
        suffix = sha1_password[5:]
        
        url = f'https://api.pwnedpasswords.com/range/{prefix}'
        response = requests.get(url)
        
        if response.status_code == 200:
            hashes = (line.split(':') for line in response.text.splitlines())
            for hash_suffix, count in hashes:
                if hash_suffix == suffix:
                    return True, int(count)
            return False, 0
        else:
            return None, 0
    except Exception as e:
        print(f"Error checking online database: {e}")
        return None, 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_password', methods=['GET', 'POST'])
def check_pass():  
    password = request.json.get('password', '')
    
    is_common, breach_count = check_password_online(password)
    
    if is_common:
        new_password = generate_strong_password()
        message = f'This password has been seen {breach_count:,} times in data breaches! Consider using the suggested password instead.'
        return jsonify({
            'is_common': True,
            'message': message,
            'suggested_password': new_password
        })
    elif is_common is None:
        return jsonify({
            'is_common': False,
            'message': 'Unable to check online database. Password complexity is okay.'
        })
    
    return jsonify({
        'is_common': False,
        'message': 'This password has not been found in known data breaches.'
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)