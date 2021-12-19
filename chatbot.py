import nltk
from nltk.chat.util import Chat,reflections


pairs = [
    [
        
        r"My name is (.*)",
        ["Hello %1, how can i help you..?",]
    ],
    [
        r"(.*)need(.*)help(.*)",
        ["how can i help you...?",]
    ],
    [
        r"(.*)love(.*)ptoduct(.*)",
        ["Please search %2 on search bar...",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name",
        ["You can call me a Jhinga.",]
    ],
    [
        r"how are you ?",
        ["I am fine, thank you! How can i help you?",]
    ],
    [
        r"(.*)fine, thank you(.*)",
        ["great to hear that, how can i help you?",]
    ],
    [
        r"(.*)doing good(.*)",
        ["That's great to hear","How can i help you?:)",]
    ],
    [
        r"(.*)online guides and courses to learn(.*)suggest?(.*)",
        ["https://pdfdrive.com is a great option to learn. You can check their website",]
    ],
    [
        r"(.*)change my(.*)information",
        ['to edit/change your information,\ngo to profile->account->account settings',]
    ],
    [
        r"(.*)register(.*)complain",
        ["What and Which type of complain",]
    ],
    [
        r"(.*)complain(.*)product",
        ["if u have any problem about product, you can contact with our Human Assistant to call on 1234566789, mail example@example.com or visit https://www.amazon.in/gp/help/customer/display.html",]
    ],
    [
        r'(.*)complain(.*)service(.*)',
        ['Please visit https://www.amazon.com/gp/help/customer/display.html?nodeId=201889700 and fill this form that we make our service better',]
    ],
    [
        r"(.*)track(.*)order(.*)",
        ["To track you order, go to your orders->select item->track order or visit https://www.amazon.in/gp/css/order-history",]
    ],
    [
        r'(.*)cancel(.*)[order|item|product](.*)',
        ['To cancel you order, go to your orders->select item->cancel order or visit https://www.amazon.in/gp/css/order-history',]
    ],
    [
        r'(.*)return(.*)',
        ['for return you order, go to your orders->select item->refund/replace item or visit https://www.amazon.in/gp/css/order-history',]
    ],
    [
        r'i(.*)refund(.*)',
        ['for refund, go to your orders->select item->click on refund/replace item or visit https://www.amazon.in/gp/css/order-history']
    ],
    [
        r'(.*)replace(.*)',
        ['for replace you order, go to your orders->select item or visit https://www.amazon.in/gp/css/order-history',]
    ],
    [
        r'(.*)change|edit(.*)address(.*)',
        ['to change or edit your address visit https://www.amazon.in/gp/css/account/address/view.html',]
    ],
    [
        r'(.*)refund [policy|process](.*)',
        ['refund will be credits in your account within 3-12 days, after 12 days if refund is not credited in your account call our Human Asistant on 1234566789 or visit https://www.amazon.in/gp/css/order-history',]
    ],
    [
        r'(.*)guarantee(.*)',
        ['Please visit https://www.amazon.com/gp/help/customer/display.html?nodeId=201889410 for A-Z information about Guarantee',]
    ],
    [
        r'(.*)digital service(.*)',
        ['Please visit in.amazonforum.com for your questions related to devices and digital services.',]
    ],
    [
        r"(.*)bye(.*)",
        ["i hope, i am helpufl for u","see you later",]
    ],
    [
        r'(.*)covid-19|corona virus|corona(.*)impact(.*)',
        ['to know about covi',]
    ],
    [
        r"(.*)thank you(.*)",
        ["I hope, I was able to answer your query for today ?",]
    ],
    [
        r"yes(.*)",
        ["I am happy to help you\ni am still learning so please write your query briefly in English in lowercase, for better understanding.\nEg. how to i change my profile information.",]
    ],
    [
        r"no(.*)",
        ["For more help\nyou can contact with our Human Assistant to call on 1234566789, mail example@example.com or visit https://www.amazon.in/gp/help/customer/display.html\nType quit to leave ",]
    ],
    [
        r"quit",
        ["It was nice talking to you. See you soon :)\nIf i am not able to solve your query, you can contact with our Human Assistant to call on 1234566789, mail example@example.com or visit https://www.amazon.in/gp/help/customer/display.html",]
    ],
    [
        r"(.*)",
        ["i don't understand, what you are trying to ask.",]
    ],

]

def hugot_bot():
    print("Hi, I'm Jhinga and I chat alot ;)\ni am still learning so please write your query briefly in English in lowercase, for better understanding.\nEg. how to i change my profile information.\nType quit to leave ")
    chat=Chat(pairs,reflections)
    chat.converse()
if __name__ == "__main__":
    hugot_bot()

