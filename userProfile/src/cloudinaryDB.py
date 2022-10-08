import cloudinary, cloudinary.uploader

class ImageDatabase():
    """ ### Klasa za uploudovanje slika na cloudinary
        #### Kao parametar uzima fajl

        - `file` -> `imageURL`
    
    """
    def __init__(self, file) -> None:

        self.file = file

        # konfiguracija
        cloudinary.config( 
        cloud_name = "dt5xxftc5", 
        api_key = "513357577797212", 
        api_secret = "rgAb0XMNQuJ6rW-INee5F9apAZ4" 
        )

    def uploadIMG(self):
        """ ## Metoda koja uplouda media file
            - `file` -> `imageURL`
        """
    
        response = cloudinary.uploader.upload(self.file, folder="webApp/")
        
        return response


