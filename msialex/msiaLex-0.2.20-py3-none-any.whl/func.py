def negation(lang):
    if(lang == 'en'):
        return ['no', 'not', 'none', 'nobody', 'nothing', 'neither', 'never', 'cannot']
    elif(lang == 'zh'):
        return {'不甚': {'intensity': -1, 'tag': 'd'},
                '别无': {'intensity': -1, 'tag': 'd'},
                '并不': {'intensity': -1, 'tag': 'd'},
                '并不会': {'intensity': -1, 'tag': 'd'},
                '并不是': {'intensity': -1, 'tag': 'd'},
                '并没有': {'intensity': -1, 'tag': 'd'},
                '并未': {'intensity': -1, 'tag': 'd'},
                '并无': {'intensity': -1, 'tag': 'd'},
                '并非': {'intensity': -1, 'tag': 'd'},
                '不': {'intensity': -1, 'tag': 'd'},
                '不是': {'intensity': -1, 'tag': 'd'},
                '不算': {'intensity': -1, 'tag': 'd'},
                '不宜': {'intensity': -1, 'tag': 'd'},
                '不再': {'intensity': -1, 'tag': 'd'},
                '不曾': {'intensity': -1, 'tag': 'd'},
                '从不': {'intensity': -1, 'tag': 'd'},
                '从来未': {'intensity': -1, 'tag': 'd'},
                '从没': {'intensity': -1, 'tag': 'd'},
                '从没有': {'intensity': -1, 'tag': 'd'},
                '从来没有': {'intensity': -1, 'tag': 'd'},
                '从未': {'intensity': -1, 'tag': 'd'},
                '从无': {'intensity': -1, 'tag': 'd'},
                '非': {'intensity': -1, 'tag': 'd'},
                '毫不': {'intensity': -1, 'tag': 'd'},
                '毫无': {'intensity': -1, 'tag': 'd'},
                '难': {'intensity': -1, 'tag': 'd'},
                '假装': {'intensity': -1, 'tag': 'd'},
                '决不': {'intensity': -1, 'tag': 'd'},
                '决不能': {'intensity': -1, 'tag': 'd'},
                '绝非': {'intensity': -1, 'tag': 'd'},
                '没': {'intensity': -1, 'tag': 'd'},
                '没法': {'intensity': -1, 'tag': 'd'},
                '没什么': {'intensity': -1, 'tag': 'd'},
                '没有': {'intensity': -1, 'tag': 'd'},
                '难以': {'intensity': -1, 'tag': 'd'},
                '难于': {'intensity': -1, 'tag': 'd'},
                '尚未': {'intensity': -1, 'tag': 'd'},
                '说不上': {'intensity': -1, 'tag': 'd'},
                '算不上': {'intensity': -1, 'tag': 'd'},
                '才怪': {'intensity': -1, 'tag': 'd'},
                '太过': {'intensity': -1, 'tag': 'd'},
                '未曾': {'intensity': -1, 'tag': 'd'},
                '无': {'intensity': -1, 'tag': 'd'},
                '无法': {'intensity': -1, 'tag': 'd'},
                '永不': {'intensity': -1, 'tag': 'd'},
                '有待': {'intensity': -1, 'tag': 'd'},
                '勿': {'intensity': -1, 'tag': 'd'},
                '不必': {'intensity': -1, 'tag': 'd'},
                '不用': {'intensity': -1, 'tag': 'd'},
                '不能': {'intensity': -1, 'tag': 'd'},
                '不会': {'intensity': -1, 'tag': 'd'},
                '不便': {'intensity': -1, 'tag': 'd'},
                '未': {'intensity': -1, 'tag': 'd'},
                '未能': {'intensity': -1, 'tag': 'd'},
                '无须': {'intensity': -1, 'tag': 'd'},
                '绝不': {'intensity': -1, 'tag': 'd'},
                '无需': {'intensity': -1, 'tag': 'd'},
                '未必': {'intensity': -1, 'tag': 'd'},
                '不怎么': {'intensity': -1, 'tag': 'd'},
                '不见得': {'intensity': -1, 'tag': 'd'},
                '木有': {'intensity': -1, 'tag': 'd'},
                '别': {'intensity': -1, 'tag': 'd'},
                '不像': {'intensity': -1, 'tag': 'd'},
                '不像是': {'intensity': -1, 'tag': 'd'},
                '不比': {'intensity': -1, 'tag': 'd'}}
        # return ['不甚', '并不', '别无', '并不会', '并不是', '并没有', '并未', '并无', '并非', '不', '不是', '不算', '不宜', '不再', '不曾', '从不', '从来未', '从没', '从没有', '从来没有', '从未', '从无', '非', '毫不', '毫无', '难', '假装', '决不', '决不能', '绝非', '没', '没法', '没什么', '没有', '难以', '难于', '尚未', '说不上', '算不上', '才怪', '太过', '未曾', '无', '无法', '永不', '有待', '勿', '不必', '不用', '不能', '不会', '不便', '未', '未能', '无须', '绝不', '无需', '未必', '不怎么', '不见得', '木有', '别', '不像', '不像是', '不比']

def intensifier(lang):
    if(lang == 'en'):
        return [
                {'high':['absolutely', 'completely', 'extremely', 'highly', 'rather', 'really', 'so', 'too', 'totally', 'utterly', 'very', 'much', 'more', 'quite', 'most', 'super']},
                {'low':['little', 'less']}
                ]
    elif(lang == 'zh'):
        return {'百分之百': {'intensity': 5, 'tag': 'd'},
                '倍加': {'intensity': 5, 'tag': 'd'},
                '入骨': {'intensity': 5, 'tag': 'd'},
                '不得了': {'intensity': 5, 'tag': 'd'},
                '不可开交': {'intensity': 5, 'tag': 'd'},
                '充分': {'intensity': 5, 'tag': 'd'},
                '到头': {'intensity': 5, 'tag': 'd'},
                '到家': {'intensity': 5, 'tag': 'd'},
                '地地道道': {'intensity': 5, 'tag': 'd'},
                '非常': {'intensity': 5, 'tag': 'd'},
                '极': {'intensity': 5, 'tag': 'd'},
                '极度': {'intensity': 5, 'tag': 'd'},
                '极端': {'intensity': 5, 'tag': 'd'},
                '极其': {'intensity': 5, 'tag': 'd'},
                '极为': {'intensity': 5, 'tag': 'd'},
                '截然': {'intensity': 5, 'tag': 'd'},
                '尽': {'intensity': 5, 'tag': 'd'},
                '绝顶': {'intensity': 5, 'tag': 'd'},
                '绝对': {'intensity': 5, 'tag': 'd'},
                '绝对化': {'intensity': 5, 'tag': 'd'},
                '莫大': {'intensity': 5, 'tag': 'd'},
                '甚为': {'intensity': 5, 'tag': 'd'},
                '十二分': {'intensity': 5, 'tag': 'd'},
                '十分': {'intensity': 5, 'tag': 'd'},
                '十足': {'intensity': 5, 'tag': 'd'},
                '完全': {'intensity': 5, 'tag': 'd'},
                '完完全全': {'intensity': 5, 'tag': 'd'},
                '万般': {'intensity': 5, 'tag': 'd'},
                '万分': {'intensity': 5, 'tag': 'd'},
                '万万': {'intensity': 5, 'tag': 'd'},
                '无比': {'intensity': 5, 'tag': 'd'},
                '无度': {'intensity': 5, 'tag': 'd'},
                '无可估量': {'intensity': 5, 'tag': 'd'},
                '无以复加': {'intensity': 5, 'tag': 'd'},
                '无以伦比': {'intensity': 5, 'tag': 'd'},
                '已极': {'intensity': 5, 'tag': 'd'},
                '已甚': {'intensity': 5, 'tag': 'd'},
                '异常': {'intensity': 5, 'tag': 'd'},
                '逾常': {'intensity': 5, 'tag': 'd'},
                '贼': {'intensity': 5, 'tag': 'd'},
                '之极': {'intensity': 5, 'tag': 'd'},
                '之至': {'intensity': 5, 'tag': 'd'},
                '至极': {'intensity': 5, 'tag': 'd'},
                '最为': {'intensity': 5, 'tag': 'd'},
                '最': {'intensity': 5, 'tag': 'd'},
                '不过': {'intensity': 4, 'tag': 'd'},
                '不少': {'intensity': 4, 'tag': 'd'},
                '不胜': {'intensity': 4, 'tag': 'd'},
                '大为': {'intensity': 4, 'tag': 'd'},
                '多': {'intensity': 4, 'tag': 'd'},
                '多多': {'intensity': 4, 'tag': 'd'},
                '多么': {'intensity': 4, 'tag': 'd'},
                '分外': {'intensity': 4, 'tag': 'd'},
                '格外': {'intensity': 4, 'tag': 'd'},
                '好不': {'intensity': 4, 'tag': 'd'},
                '何等': {'intensity': 4, 'tag': 'd'},
                '不是一般': {'intensity': 4, 'tag': 'd'},
                '很': {'intensity': 4, 'tag': 'd'},
                '好': {'intensity': 4, 'tag': 'd'},
                '很是': {'intensity': 4, 'tag': 'd'},
                '很多': {'intensity': 4, 'tag': 'd'},
                '可': {'intensity': 4, 'tag': 'd'},
                '颇': {'intensity': 4, 'tag': 'd'},
                '颇为': {'intensity': 4, 'tag': 'd'},
                '甚': {'intensity': 4, 'tag': 'd'},
                '实在': {'intensity': 4, 'tag': 'd'},
                '太': {'intensity': 4, 'tag': 'd'},
                '太甚': {'intensity': 4, 'tag': 'd'},
                '特': {'intensity': 4, 'tag': 'd'},
                '特别': {'intensity': 4, 'tag': 'd'},
                '尤': {'intensity': 4, 'tag': 'd'},
                '尤其': {'intensity': 4, 'tag': 'd'},
                '尤为': {'intensity': 4, 'tag': 'd'},
                '着实': {'intensity': 4, 'tag': 'd'},
                '真': {'intensity': 4, 'tag': 'd'},
                '大不了': {'intensity': 3, 'tag': 'd'},
                '更': {'intensity': 3, 'tag': 'd'},
                '更加': {'intensity': 3, 'tag': 'd'},
                '更进一步': {'intensity': 3, 'tag': 'd'},
                '更为': {'intensity': 3, 'tag': 'd'},
                '较': {'intensity': 3, 'tag': 'd'},
                '较为': {'intensity': 3, 'tag': 'd'},
                '进一步': {'intensity': 3, 'tag': 'd'},
                '那般': {'intensity': 3, 'tag': 'd'},
                '那么': {'intensity': 3, 'tag': 'd'},
                '那样': {'intensity': 3, 'tag': 'd'},
                '如斯': {'intensity': 3, 'tag': 'd'},
                '益': {'intensity': 3, 'tag': 'd'},
                '益发': {'intensity': 3, 'tag': 'd'},
                '尤甚': {'intensity': 3, 'tag': 'd'},
                '逾': {'intensity': 3, 'tag': 'd'},
                '愈': {'intensity': 3, 'tag': 'd'},
                '愈发': {'intensity': 3, 'tag': 'd'},
                '愈加': {'intensity': 3, 'tag': 'd'},
                '愈来愈': {'intensity': 3, 'tag': 'd'},
                '愈益': {'intensity': 3, 'tag': 'd'},
                '远远': {'intensity': 3, 'tag': 'd'},
                '越发': {'intensity': 3, 'tag': 'd'},
                '越加': {'intensity': 3, 'tag': 'd'},
                '越来越': {'intensity': 3, 'tag': 'd'},
                '越是': {'intensity': 3, 'tag': 'd'},
                '这般': {'intensity': 3, 'tag': 'd'},
                '这样': {'intensity': 3, 'tag': 'd'},
                '足足': {'intensity': 3, 'tag': 'd'},
                '不为过': {'intensity': 3, 'tag': 'd'},
                '超': {'intensity': 3, 'tag': 'd'},
                '忒': {'intensity': 3, 'tag': 'd'},
                '多多少少': {'intensity': -2, 'tag': 'd'},
                '好生': {'intensity': -2, 'tag': 'd'},
                '或多或少': {'intensity': -2, 'tag': 'd'},
                '略': {'intensity': -2, 'tag': 'd'},
                '略加': {'intensity': -2, 'tag': 'd'},
                '略略': {'intensity': -2, 'tag': 'd'},
                '略微': {'intensity': -2, 'tag': 'd'},
                '略为': {'intensity': -2, 'tag': 'd'},
                '蛮': {'intensity': -2, 'tag': 'd'},
                '稍': {'intensity': -2, 'tag': 'd'},
                '稍稍': {'intensity': -2, 'tag': 'd'},
                '稍为': {'intensity': -2, 'tag': 'd'},
                '稍微': {'intensity': -2, 'tag': 'd'},
                '稍许': {'intensity': -2, 'tag': 'd'},
                '挺': {'intensity': -2, 'tag': 'd'},
                '未免': {'intensity': -2, 'tag': 'd'},
                '相当': {'intensity': -2, 'tag': 'd'},
                '一些': {'intensity': -2, 'tag': 'd'},
                '些微': {'intensity': -2, 'tag': 'd'},
                '一点': {'intensity': -2, 'tag': 'd'},
                '一点儿': {'intensity': -2, 'tag': 'd'},
                '一点点': {'intensity': -2, 'tag': 'd'},
                '有点': {'intensity': -2, 'tag': 'd'},
                '有点点': {'intensity': -2, 'tag': 'd'},
                '有点儿': {'intensity': -2, 'tag': 'd'},
                '有些': {'intensity': -2, 'tag': 'd'},
                '半点': {'intensity': -2, 'tag': 'd'},
                '不大': {'intensity': -2, 'tag': 'd'},
                '不丁点儿': {'intensity': -2, 'tag': 'd'},
                '轻度': {'intensity': -2, 'tag': 'd'},
                '丝毫': {'intensity': -2, 'tag': 'd'},
                '微': {'intensity': -2, 'tag': 'd'},
                '相对': {'intensity': -2, 'tag': 'd'}}
        # return ['百分之百','倍加','入骨','不得了','不可开交','充分','到头','到家','地地道道','非常','极','极度','极端','极其','极为','截然','尽','绝顶','绝对','绝对化','莫大','甚为','十二分','十分','十足','完全','完完全全','万般','万分','万万','无比','无度','无可估量','无以复加','无以伦比','已极','已甚','异常','逾常','贼','之极','之至','至极','最为','最','不过','不少','不胜','大为','多','多多','多么','分外','格外','好不','何等','不是一般','很','好','很是','很多','可','颇','颇为','甚','实在','太','太甚','特','特别','尤','尤其','尤为','着实','真','大不了','更','更加','更进一步','更为','较','较为','进一步','那般','那么','那样','如斯','益','益发','尤甚','逾','愈','愈发','愈加','愈来愈','愈益','远远','越发','越加','越来越','越是','这般','这样','足足','不为过','超','忒','多多少少','好生','或多或少','略','略加','略略','略微','略为','蛮','稍','稍稍','稍为','稍微','稍许','挺','未免','相当','一些','些微','一点','一点儿','一点点','有点','有点点','有点儿','有些','半点','不大','不丁点儿','轻度','丝毫','微','相对']

def disjunction(lang):
    if(lang == 'en'):
        return ['but', 'however', 'in contrast', 'instead', 'whereas', 'except that', 'on the contrary', 'conversely', 'nevertheless', 'although', 'alternatively']
    elif(lang == 'zh'):
        return {'但': {'intensity': 3, 'tag': 'c'},
                '但是': {'intensity': 3, 'tag': 'c'},
                '却': {'intensity': 3, 'tag': 'c'},
                '然而': {'intensity': 3, 'tag': 'c'},
                '而': {'intensity': 3, 'tag': 'c'},
                '偏偏': {'intensity': 3, 'tag': 'c'},
                '只是': {'intensity': 3, 'tag': 'c'},
                '就是': {'intensity': 3, 'tag': 'c'},
                '不过': {'intensity': 3, 'tag': 'c'},
                '可是': {'intensity': 3, 'tag': 'c'},
                '不料': {'intensity': 3, 'tag': 'c'},
                '岂知': {'intensity': 3, 'tag': 'c'}}
        # return ['但', '但是', '却', '然而', '而', '偏偏', '只是', '就是', '不过', '可是', '不料', '岂知']

    