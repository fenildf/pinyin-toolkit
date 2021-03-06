# First column:
#   Support level (0 = none, 1 = partial, 2 = full)
#
# Second column:
#   ISO 639 languages (http://ftp.ics.uci.edu/pub/ietf/http/related/iso639.txt).
#   This is the actual code we consider to code for the language.
#
# Third column:
#   ISO 3166-1 country code. This is only use to select a flag icon for the preferences combo box.
#   I haven't bothered going through giving every language one of these yet.
#
#  A language with a flat next to it has been tested to have at least some support (i.e. google translate)
#  A language that is commented out has zero support (i.e. google translate cna't handle it)
#  Chinese is also commented out (because there is no point is transalting Chinese-Chinese)
#
# albanian has support, missing from list
# 
# Fourth column:
#   Human readable language name.
languages = [
    #(0, "aa", None, "Afar"),               # no support as of 2009-06-06
    #(0, "ab", None, "Abkhazian"),      # no support as of 2009-06-06
    #(0, "af", None, "Afrikaans"),      # no support as of 2009-06-06
    #(0, "am", None, "Amharic"),     # no support as of 2009-06-06
    (0, "ar", "ar", "Arabic"),            # support: gtrans
    (0, "as", None, "Assamese"),
    (0, "ay", None, "Aymara"),
    (0, "az", None, "Azerbaijani"),
    (0, "ba", None, "Bashkir"),
    (0, "be", None, "Byelorussian"),
    (0, "bg", None, "Bulgarian"),
    (0, "bh", None, "Bihari"),
    (0, "bi", None, "Bislama"),
    (0, "bn", None, "Bengali"),
    #(0, "bo", "cn", "Tibetan"),     # no support as of 2009-06-06
    (0, "br", None, "Breton"),
    (0, "ca", None, "Catalan"),
    (0, "co", None, "Corsican"),
    (0, "cs", None, "Czech"),
    (0, "cy", None, "Welsh"),
    (0, "da", None, "Danish"),
    (2, "de", "de", "German"),
    (0, "dz", None, "Bhutani"),
    (0, "el", "gr", "Greek"),       # support: gtrans
    (2, "en", "gb", "English"),     # full suport: gtrans, CC-CEDICT
    (0, "eo", None, "Esperanto"),
    (0, "es", None, "Spanish"),
    (0, "et", None, "Estonian"),
    (0, "eu", None, "Basque"),
    (0, "fa", None, "Persian"),
    (0, "fi", "FI", "Finnish"),       # support: gtrans
    (0, "fj", None, "Fiji"),
    (0, "fo", None, "Faroese"),
    (1, "fr", "fr", "French"),      # hybri support: gtrans, CFDICT
    (0, "fy", None, "Frisian"),
    (0, "ga", None, "Irish"),
    (0, "gd", None, "Scots Gaelic"),
    (0, "gl", None, "Galician"),
    (0, "gn", None, "Guarani"),
    (0, "gu", None, "Gujarati"),
    (0, "ha", None, "Hausa"),
    (0, "he", None, "Hebrew"),
    #(0, "hi", "in", "Hindi"),     # supoprt: gtrans
    (0, "hr", None, "Croatian"),
    (0, "hu", None, "Hungarian"),
    (0, "hy", None, "Armenian"),
    (0, "ia", None, "Interlingua"),
    (0, "id", None, "Indonesian"),
    (0, "ie", None, "Interlingue"),
    (0, "ik", None, "Inupiak"),
    (0, "is", None, "Icelandic"),
    (0, "it", "it", "Italian"),     # supoprt: gtrans
    (0, "iu", None, "Inuktitut"),
    (0, "ja", "jp", "Japanese"),
    (0, "jw", None, "Javanese"),
    (0, "ka", None, "Georgian"),
    (0, "kk", None, "Kazakh"),
    (0, "kl", None, "Greenlandic"),
    (0, "km", None, "Cambodian"),
    (0, "kn", None, "Kannada"),
    (0, "ko", None, "Korean"),
    (0, "ks", None, "Kashmiri"),
    (0, "ku", None, "Kurdish"),
    (0, "ky", None, "Kirghiz"),
    (0, "la", None, "Latin"),
    (0, "ln", None, "Lingala"),
    (0, "lo", None, "Laothian"),
    (0, "lt", None, "Lithuanian"),
    (0, "lv", None, "Latvian"),
    (0, "mg", None, "Malagasy"),
    (0, "mi", None, "Maori"),
    (0, "mk", None, "Macedonian"),
    #(0, "ml", "my", "Malayalam"),     # no support as of 2009-06-06
    (0, "mn", None, "Mongolian"),
    (0, "mo", None, "Moldavian"),
    (0, "mr", None, "Marathi"),
    (0, "ms", None, "Malay"),
    (0, "mt", None, "Maltese"),
    (0, "my", None, "Burmese"),
    (0, "na", None, "Nauru"),
    (0, "ne", None, "Nepali"),
    (0, "nl", None, "Dutch"),
    (0, "no", None, "Norwegian"),
    (0, "oc", None, "Occitan"),
    (0, "om", None, "(Afan) Oromo"),
    (0, "or", None, "Oriya"),
    (0, "pa", None, "Punjabi"),
    (0, "pl", None, "Polish"),
    (0, "ps", None, "Pashto, Pushto"),
    (0, "pt", None, "Portuguese"),
    (0, "qu", None, "Quechua"),
    (0, "rm", None, "Rhaeto-Romance"),
    (0, "rn", None, "Kirundi"),
    (0, "ro", None, "Romanian"),
    (0, "ru", None, "Russian"),
    (0, "rw", None, "Kinyarwanda"),
    (0, "sa", None, "Sanskrit"),
    (0, "sd", None, "Sindhi"),
    (0, "sg", None, "Sangho"),
    (0, "sh", None, "Serbo-Croatian"),
    (0, "si", None, "Sinhalese"),
    (0, "sk", None, "Slovak"),
    (0, "sl", None, "Slovenian"),
    (0, "sm", None, "Samoan"),
    (0, "sn", None, "Shona"),
    (0, "so", None, "Somali"),
    (0, "sq", None, "Albanian"),
    (0, "sr", None, "Serbian"),
    (0, "ss", None, "Siswati"),
    (0, "st", None, "Sesotho"),
    (0, "su", None, "Sundanese"),
    (0, "sv", None, "Swedish"),
    (0, "sw", None, "Swahili"),
    (0, "ta", None, "Tamil"),
    (0, "te", None, "Telugu"),
    (0, "tg", None, "Tajik"),
    (0, "th", "th", "Thai"),
    (0, "ti", None, "Tigrinya"),
    (0, "tk", None, "Turkmen"),
    (0, "tl", None, "Tagalog"),
    (0, "tn", None, "Setswana"),
    (0, "to", None, "Tonga"),
    (0, "tr", None, "Turkish"),
    (0, "ts", None, "Tsonga"),
    (0, "tt", None, "Tatar"),
    (0, "tw", None, "Twi"),
    (0, "ug", None, "Uighur"),
    (0, "uk", None, "Ukrainian"),
    (0, "ur", None, "Urdu"),
    (0, "uz", None, "Uzbek"),
    (0, "vi", None, "Vietnamese"),
    #(0, "vo", None, "Volapuk"),     # no support as of 2009-06-06
    (0, "wo", None, "Wolof"),
    (0, "xh", None, "Xhosa"),
    (0, "yi", None, "Yiddish"),
    (0, "yo", None, "Yoruba"),
    (0, "za", None, "Zhuang"),
    #(0, "zh", "cn", "Chinese"),
    (0, "zu", None, "Zulu")
  ]