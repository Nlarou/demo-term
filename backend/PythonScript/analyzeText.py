import sys
import numpy as np
import pickle
import os
dir_path = os.path.dirname(os.path.realpath(__file__))


target = {"117": "You waive your right to a class action.", "118": "You waive your moral rights", "119": "Your feedback is invited regarding changes to the terms.", "120": "Critical changes to the terms are made without user involvement", "121": " Terms may be changed any time at their discretion, without notice to you ", "122": "The terms may be changed at any time, but you will receive notification of the changes", "123": "When the service wants to change its terms, you are notified a week or more in advance.", "124": "When the service wants to make a material change to its terms, you are notified at least 30 days in advance", "126": "First-party cookies are used", "127": "Third party cookies are employed, but with opt out instructions", "128": "Third-party cookies are used for advertising", "129": "This service tracks you on other websites", "130": "A license is kept on user-generated content even after you close your account", "131": "Content is published under a free license instead of a bilateral one", "132": "The copyright license maintained by the service over your data and/or content is broader than necessary.", "134": "Your content can be licensed to third parties", "135": "Copyright license limited for the purposes of that same service but transferable and sublicenseable", "136": "The copyright license that you grant this service is limited to the parties that make up the service's broader platform.", "138": "Instructions are provided on how to submit a copyright claim", "139": "Your content can be distributed through any media known now or in the future", "140": "You can retrieve an archive of your data", "141": "Inconvenient process for obtaining personal data", "142": "only for your individual use", "143": "This service is only available for use individually and non-commercially.", "144": "Other applicable rules, terms, conditions or guidelines", "145": "You are solely responsible for claims made against the service and agree to indemnify and hold harmless the service.", "146": "You agree to defend, indemnify, and hold the service harmless in case of a claim related to your use of the service", "147": "Defend, indemnify, hold harmless; survives termination", "148": "You are responsible for maintaining the security of your account and for the activities on your account", "149": "Any liability on behalf of the service is only limited to the fees you paid as a user", "150": "Spidering, crawling, or accessing the site through any automated means is not allowed", "151": "You have a reduced time period to take legal action against the service", "152": "This service is only available to users over a certain age", "154": "This service cannot be held responsible for disputes that you may have with other users", "155": "If you are the target of a copyright holder's take down notice, this service gives you the opportunity to defend yourself", "156": "Per the service's terms, you may not express negative opinions about them", "157": "Your use is throttled", "159": "You will be notified about website maintenance", "160": "No guarantee is given regarding quality", "161": "You are entitled to a refund if certain thresholds or standards are not met by the service", "162": "The service has a no refund policy", "163": "The court of law governing the terms is in location X", "164": "This service reserves the right to disclose your personal information without notifying you", "165": "The service promises to inform and/or notify you regarding government inquiries that may involve your personal data", "166": "This service shares your personal data with third parties that are not essential to its operation", "167": "Third parties are not allowed to access your personal information without a legal basis", "168": "The service is not transparent regarding government requests or inquiries that may involve your data. ", "169": "The service is transparent regarding government requests or inquiries that may involve your data.", "170": "You have the right to leave this service at any time", "173": "This service retains rights to your content even after you stop using your account", "174": "This service holds onto content that you've deleted", "175": "You can delete your content from this service", "178": "Logs are kept for an undefined period of time", "180": "This service can use your content for all their existing and future services", "182": "If you offer suggestions to the service, they become the owner of the ideas that you give them", "183": "You maintain ownership of your content", "184": "This service provides a way for you to export your data", "185": "Your personal information is used for many different purposes", "186": "This service assumes no liability for unauthorized access to your personal information", "187": "Your data may be processed and stored anywhere in the world", "188": "This service gives your personal data to third parties involved in its operation", "189": "Your private content may be accessed by people working for the service", "190": "Your personal data is aggregated into statistics", "191": "Only aggregate data is given to third parties", "192": "IP addresses of website visitors are not tracked", "193": "Your personal data is not sold", "195": "You can request access, correction and/or deletion of your data", "196": "Your personal data is used for limited purposes", "197": "Archives of their agreements are provided so that changes can be viewed over time", "198": "The terms for this service are translated into different languages", "199": "The terms for this service are easy to read", "200": "Separate policies are employed for different parts of the service", "201": "Your account can be deleted without prior notice and without a reason", "202": "Specific content can be deleted without reason and may be removed without prior notice", "203": "They may stop providing the service at any time", "204": "User suspension from the service will be fair and proportionate.", "205": "Your account can be suspended for several reasons", "206": "30 days of notice are given before closing your account", "207": "Third parties are involved in operating the service", "208": "Many third parties are involved in operating the service", "209": "You are warned of the potential consequences related to third-party access", "210": "Third parties used by the service are bound by confidentiality obligations", "211": "Extra data may be collected about you through promotions", "213": "You are not allowed to use pseudonyms, as trust and transparency between users regarding their identities is relevant to the service.", "214": "You must provide your legal name, pseudonyms are not allowed", "215": " Pseudonyms are allowed", "216": "Your personal data is used for advertising", "217": "Tracking pixels are used in service-to-user communication", "218": "You are not being tracked", "219": "You can opt out of targeted advertising", "220": "Your personal data is used to employ targeted third-party advertising", "221": "The service deletes tracking data after a period of time and allows you to opt out", "222": "You can choose the copyright license", "223": "You can opt out of promotional communications", "225": "You can choose with whom you share content", "226": "Information is provided about security practices", "227": "Information is provided about how your personal data is used", "228": "Details are provided about what kind of information they collect", "229": "You cannot distribute or disclose your account to third parties", "230": "You must create an account to use this service", "231": "You are informed about the risk of publishing personal info online", "232": "A free help desk is provided",
          "233": "Do Not Track (DNT) headers are ignored and you are tracked anyway even if you set this header.", "234": "They store data on you even if you did not interact with the service", "237": "You agree to comply with the law of the service's country", "238": "You agree not to submit illegal content", "239": "Private messages can be read", "241": "The court of law governing the terms is in a jurisdiction that is friendlier to user privacy protection.", "242": "The court of law governing the terms is in a jurisdiction that is less friendly to user privacy protection.", "243": "Your personal data may be sold or otherwise transferred as part of a bankruptcy proceeding or other type of financial transaction", "276": "The service can intervene in user disputes", "277": "Conditions may change, but your continued acceptance is not inferred from an earlier acceptance", "278": "The service is not responsible for linked or (clearly) quoted content from third-party content providers", "279": "This service assumes no responsibility and liability for the contents of links to other websites", "280": "You agree not to use the service for illegal purposes", "281": "You are prohibited from sending chain letters, junk mail, spam or any unsolicited messages", "283": "You agree not to submit libelous, harassing or threatening content", "284": "You are prohibited from attempting to gain unauthorized access to other computer systems", "285": "You shall not interfere with another person's enjoyment of the service", "286": "The service is provided 'as is' and to be used at your sole risk", "287": "The service provider makes no warranty regarding uninterrupted, timely, secure or error-free service", "288": "The service does not guarantee accuracy or reliability of the information provided", "289": "The service does not guarantee that software errors will be corrected", "290": "This service does not guarantee that it or the products obtained through it meet your expectations or requirements", "291": "You are responsible for any risks, damages, or losses that may incur by downloading materials", "292": "This service does not condone any ideas contained in its user-generated contents", "293": "This service assumes no liability for any losses or damages resulting from any matter relating to the service", "294": "Invalidity of any portion of the Terms of Service does not entail invalidity of its remainder", "295": "Failure to enforce any provision of the Terms of Service does not constitute a waiver of such provision", "296": "Your information is only shared with third parties when given specific consent", "297": "Information is provided about how they collect personal data", "299": "The service informs you that its privacy policy does not apply to third party websites", "300": "A complaint mechanism is provided for the handling of personal data", "301": "The service reviews its privacy policy on a regular basis", "303": "The data retention period is kept to the minimum necessary for fulfilling its purposes", "304": "The service may keep a secure, anonymized record of your data for analytical purposes even after the data retention period", "305": "The service will resist legal requests for your information where reasonably possible", "306": " A list of all cookies set by the website is provided", "307": " You are being tracked via social media cookies/pixels", "310": "If you are the target of a copyright claim, your content may be removed", "312": "Two factor authentication is provided for your account", "313": "User accounts can be terminated after having been in breach of the terms of service repeatedly", "314": "You are prohibited from posting content which promotes violence or politically or religiously extremist values.", "315": "The posting of pornographic content is prohibited", "316": "Political discussions or campaining are prohibited", "319": "Users who have been permanently banned from this service are not allowed to re-register under a new account", "320": "No need to register", "321": "Promises will be kept after a merger or acquisition", "322": "App required for this service requires broad device permissions", "323": "You are tracked via web beacons, tracking pixels, browser fingerprinting, and/or device fingerprinting", "324": "Alternative accounts are not allowed", "325": "Third-party cookies are used for statistics", "326": "Your profile is combined across various products", "327": "Your identity is used in ads that are shown to other users", "328": "Usernames can be rejected or changed for any reason", "329": "You should revisit the terms periodically, although in case of material changes, the service will notify", "331": "There is a date of the last update of the agreements", "332": "This service offers a symbolic but nonbinding statement about a matter of opinion, ethics, society, or politics", "333": "Some personal data may be kept for business interests or legal obligations", "335": "You aren\u2019t forced into binding arbitration in case of disputes", "336": "Your personal data may be used for marketing purposes", "337": "You can opt out of providing personal information to third parties", "338": "You can limit how your information is used by third-parties and the service", "339": "You are forced into binding arbitration in case of disputes", "372": "User-generated content is encrypted, and this service cannot decrypt it", "373": "This service may collect, use, and share location data", "374": "The cookies used by this service do not contain information that would personally identify you", "375": "Blocking first party cookies may limit your ability to use the service", "376": "Many different types of personal data are collected", "377": "Your content can be deleted if you violate the terms", "379": "User-generated content can be blocked or censored for any reason", "382": "Information is gathered about you through third parties", "383": "Your browser's Do Not Track (DNT) headers are respected", "384": "You authorise the service to charge a credit card supplied on re-occurring basis", "387": "This service tracks which web page referred you to it", "390": "If you offer suggestions to the service, they may use that without your approval or compensation, but they do not become the owner", "391": "You will be notified if personal data has been affected by data breaches", "393": "The service will only respond to government requests that are reasonable", "394": "You cannot delete your contributions, but it makes sense for this service", "395": "Your browsing history can be viewed by the service", "396": "Your Personal data may be sold unless you opt out", "397": "Your biometric data is collected", "398": "This service has a no refund policy with some exceptions", "399": "Your IP address is collected, which can be used to view your approximate location", "400": "This service receives your precise location through GPS coordinates", "402": "The service has non-exclusive use of your content", "403": "Instead of asking directly, this Service will assume your consent merely from your usage.", "404": "This Service provides a list of Third Parties involved in its operation.", "406": "An onion site accessible over Tor is provided", "407": "Content you post may be edited by the service for any reason", "408": "This service informs you that its Terms of Service does not apply to third party websites", "409": "You must provide your identifiable information", "411": "Your data is processed and stored in a country that is less friendly to user privacy protection", "444": "The publishing of personally identifiable information without the owner\u2019s consent is not allowed", "478": "This service still tracks you even if you opted out from tracking", "479": "You aren\u2019t allowed to remove or edit user-generated content", "481": "The service claims to be GDPR compliant for European users", "482": "The service claims to be CCPA compliant for California users", "484": "You must report to the service any unauthorized use of your account or any breach of security", "486": "Minors must have the authorization of their legal guardians to use the service", "489": "Voice data is collected and shared with third-parties", "490": " The service is only available in some countries approved by its government", "493": "This service is a subsidiary of Company X"}


def get_top_k_predictions(model, X_test, k):

    # get probabilities instead of predicted labels, since we want to collect top 3
    probs = model.predict_proba(X_test)

    # GET TOP K PREDICTIONS BY PROB - note these are just index
    best_n = np.argsort(probs, axis=1)[:, -k:]
    # GET CATEGORY OF PREDICTIONS
    preds = [[model.classes_[predicted_cat]
              for predicted_cat in prediction] for prediction in best_n]

    preds = [item[::-1] for item in preds]

    return preds


def predict(text):
    loaded_model = pickle.load(open(dir_path+"\\model.pkl", 'rb'))
    loaded_transformer = pickle.load(open(dir_path+"\\transformer.pkl", 'rb'))
    test_features = loaded_transformer.transform([text])
    preds = get_top_k_predictions(loaded_model, test_features, 3)
    pred = [target[str(item)] for item in preds[0]]
    return pred


print(predict(sys.argv[1]), end="")
