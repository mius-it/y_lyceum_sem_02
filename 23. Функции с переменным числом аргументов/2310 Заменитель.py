def placeholder(*sentences, **keys):
    hits = {}
    for k in keys.values():
        k_words = k.split()
        kl = len(k_words)
        for s in sentences:
            s_words = s.split()
            sl = len(s_words)
            if sl == kl:
                for i in range(kl):
                    if k_words[i] == '|_' and not s_words[i][0].isupper():
                        break
                    if k_words[i][-1] in ',.!?-' and k_words[i][-1] != s_words[i][-1]:
                        break
                else:
                    if k in hits:
                        hits[k].append(s)
                    else:
                        hits[k] = []
                        hits[k].append(s)
    for h in hits:
        hits[h].sort()
    return hits


# lines = ["Look at the boy, he has a toy.",
#          "Look at me.", "I am happy.",
#          "Here is the kitchen where Mother cooks for me.",
#          "What are little boys made of?",
#          "What are little girls made of?",
#          "Look at the girl, she has a doll."]
# holders = {"h1": "|_ _ _ _, _ _ _ _.",
#            "h2": "|_ _ _.", "h3": "|_ _ _ _ _ _?"}
# for k, v in placeholder(*lines, **holders).items():
#     print(k, "->", *v)
