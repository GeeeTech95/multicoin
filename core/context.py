from django.core.exceptions import ObjectDoesNotExist


def core(request) :
    prepend = "https://" if request.is_secure() else "http://"
    host = request.get_host()
    #reg_link  = prepend + host + request.user.user_admin.reg_link
    ctx = {}

    ctx['liquidity'] = 53199180
    ctx['site_name_verbose'] = "Multicoin Crypto Investment"
    ctx['site_name'] = "Multicoin Crypto Investment"
    ctx['site_name_full'] = "Multicoin Crypto Investment"
    ctx['support_email'] = "support@multicoin.com"
    ctx['site_email'] = "support@multicoin.com"
    ctx['site_phone'] = "+3594858"
    ctx['site_whatsapp_no'] = "+6665865690"
    ctx['site_address'] = "No 23 winston road new york"
    ctx['ltc_wallet_address'] = "LL9nbteEzEguwuzLWuTiH66YnKEbHsa8ko"
    ctx['usdt_bep20_wallet_address'] = "0x1aeeffb9bebfa454682db27ba57e3e6079c401b8"
    ctx['usdt_trc20_wallet_address'] =  "TUor2dyPNeTHJ4YUfUQC1u3bwNQjvfamR4"
    ctx['eth_wallet_address'] = "0x1aeeffb9bebfa454682db27ba57e3e6079c401b8"
    ctx['btc_wallet_address'] = "1NNxCVT4S3MzifmGzfmj3GkV7X5gF55PQe"
    ctx['bnb_wallet_address'] = "0xf4ae2f6cb341cea26ee41ecfdf31c65513dd2bcf"
    
    return ctx  


    
        