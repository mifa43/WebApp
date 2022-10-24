import cloudinary, cloudinary.uploader
import os

class ImageDatabase():
    """ ### Klasa za uploudovanje slika na cloudinary
        #### Kao parametar uzima fajl

        - `file` -> `imageURL`
    
    """
    def __init__(self, file) -> None:

        self.file = file

        # konfiguracija
        cloudinary.config( 
        cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"), 
        api_key = os.getenv("CLOUDINARY_API_KEY"), 
        api_secret = os.getenv("CLOUDINARY_API_SECRET")
        )

    def uploadIMG(self):
        """ ## Metoda koja uplouda media file
            - `file` -> `imageURL`
        """
    
        response = cloudinary.uploader.upload(self.file, folder="webApp/")
        
        return response