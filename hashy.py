#!/usr/bin/env python

dictionary = {}

word_list = ["cat", "dog"]
language_list = ["english", "russian"]

dictionary = {
    "english": {
        "cat": "an annoying creature that is cuddly and dumb",
        "dog": "dumber than cats also smells really bad all the time"
    }, "russian": {
        "cat": "horosho",
        "dog": "ni horosho"
    }
}


# dictionary["english"] = {
#   "cat": "an annoying...",
#   "dog": "dumber..."


for word in word_list:
    for language in language_list:
        print word + ": " + language + ": " + dictionary[language][word]
