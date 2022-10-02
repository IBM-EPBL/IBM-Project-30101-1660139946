
from flask import Flask ,redirect,url_for,render_templte,json
import os
app = flask(__name__)
food_items={"1":"apple","2":"bamnana","3":"watermelon","4":"pinapple","6":"cherry"}
@app.route('/data',methods=['POST','GET'])
def api():
    if request.method=='GET':
        return food_items
    if request.method=='POST':
        data ='request.json'
        food_items.update(data)
        return "data is inserted"

    @spp.route('/data/<id>',method=["PUT"])
    def update(id):
        data request.form['item']
        food_items[str(id)]=data
        return "data updated"

      @spp.route('/data/<id>',method=["DELETE"])
    def delete(id):
        food_items.pop(str(id))
        return "data deleted"
        if __name__=='main':
           port = os.environment .get('FLASK_PORT')
           port = int(port)

           app.run(post=post,host='0.0.0.0')
           app.run(debug=True)

