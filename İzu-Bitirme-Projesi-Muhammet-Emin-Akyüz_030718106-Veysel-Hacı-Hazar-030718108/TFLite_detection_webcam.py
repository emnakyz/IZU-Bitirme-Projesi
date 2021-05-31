
            
            def thread_function():
                #resim kaydetme
                now = datetime.now()
                nowstr = now.strftime("%d%m%Y%H%M%S")
                imageName = 'img'+ str(nowstr) + '.png'
                cv2.imwrite(imageName,frame)
                #resmi upload etme
                PATH = imageName
                im = pyimgur.Imgur(CLIENT_ID)
                uploaded_image = im.upload_image(PATH, title=imageName)
                #resmi silme
                if os.path.exists(imageName):
                      os.remove(imageName)
                else:
                      print("The file does not exist")
                print(uploaded_image.title)
                print(uploaded_image.link)
                print(uploaded_image.size)
                print(uploaded_image.type)
                
                #sunucuya kaydetme
                def thread_function3():
                    myclient = pymongo.MongoClient("mongodb+srv://fotokapan:Veysel.34@cluster0.mrsvk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
                    mydb = myclient["Cluster0"]
                    mycol = mydb["loglar"]
                    mydict = {'object_name': object_name, 'img_url': uploaded_image.link, 'rate': str(int(scores[i]*100))}
                    x = mycol.insert_one(mydict)
                th = threading.Thread(target=thread_function3)
                th.start()
                def thread_function2():
                    token = "1216953701:AAEf-h8E7vWoNCp-cE-2JLbNh-s1CQqqiOc"
                    chat_id = "@fotokapan"
                    url = f'https://api.telegram.org/bot'+token+'/sendMessage'
                    data = {'chat_id': chat_id, 'text': uploaded_image.link}
                    requests.post(url, data).json()
                    
                th = threading.Thread(target=thread_function2)
                th.start()
                
            if object_name == "person" or object_name == "dog" or object_name == "cat":
                th = threading.Thread(target=thread_function)
                th.start()
                #ses oynatma
                if object_name == "person":
                    pygame.mixer.init()
                    pygame.mixer.music.load("ses.wav")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                        
                if object_name == "dog":
                    pygame.mixer.init()
                    pygame.mixer.music.load("ses.wav")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                
                
                if object_name == "cat":
                    pygame.mixer.init()
                    pygame.mixer.music.load("ses.wav")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                 
            

