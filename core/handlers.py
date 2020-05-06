import base64


class Handlers:
    """ All the handlers and support functiosn to make a math or modify things """
    
    @staticmethod
    def encode_keys(**kwargs) -> str:
        """ Params: client_key, client_secret, method\n
            returns: client_key and client_secret encoded in base64 
        """
        try:
            method        = kwargs.pop('method'       ,'ascii')
            client_key    = kwargs.pop('client_key'   , None)
            client_secret = kwargs.pop('client_secret', None)
        except:
            raise

        if client_key and client_secret:
            key_secret = '{}:{}'.format(
                client_key, 
                client_secret
            ).encode(method)
            
            b64_encoded_key = base64.b64encode(key_secret)
            b64_encoded_key = b64_encoded_key.decode(method)

            return b64_encoded_key
        else:
            tb = sys.exc_info()[2]
            raise TypeError("args: client_key or client_secret is a invalid value or is empty").with_traceback(tb)

