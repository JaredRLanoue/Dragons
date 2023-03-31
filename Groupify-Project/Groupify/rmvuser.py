from flask import Flask, jsonify, request

app = Flask(__name__)

# assume that you have a group model with a list of group objects

# Endpoint for removing a user from a group
@app.route('/groups/<int:group_id>/remove-user', methods=['POST'])
def remove_user_from_group(group_id):
    # Retrieve user ID from request body
    user_id = request.json.get('user_id')
    
    # Retrieve group by ID from group model
    group = next((group for group in groups if group['id'] == group_id), None)
    
    if group is None:
        return jsonify({'error': 'Group not found'}), 404
    
    # Retrieve user by ID from the group's list of users
    user = next((user for user in group['users'] if user['id'] == user_id), None)
    
    if user is None:
        return jsonify({'error': 'User not found in group'}), 404
    
    # Remove user from the group's list of users
    group['users'].remove(user)
    
    return jsonify({'message': 'User removed from group'}), 200

# Start the server
if __name__ == '__main__':
    app.run(debug=True)
