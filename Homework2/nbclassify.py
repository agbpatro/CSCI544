import os
import sys
import math
import fnmatch
import string
from os import listdir
from os.path import isfile, join
fn = sys.argv[1]
prefix_hash = {}
prefix_hash["positive"]  = "p_"
prefix_hash["negative"]  = "n_"
prefix_hash["truthful"]  = "t_"
prefix_hash["deceptive"] = "d_"
stop_words = ['the','be','and','an','i','he','it','is','of','in','or','was','he','she','av','aug','august','where','week','we','hors','wc','us','am','at','ci','my','nd','rri','sw','to','aaa','abd','ae','fl','im','its']
#stop_words = []
#single_char = list(string.ascii_lowercase)
#online_stop = ['a','about','above','after','again','against','all','am','an','and','any','are','arent','as','at','be','because','been','before','being','below','between','both','but','by','cant','cannot','could','couldnt','did','didnt','do','does','doesnt','doing','dont','down','during','each','few','for','from','further','had','hadnt','has','hasnt','have','havent','having','he','hed','hell','hes','her','here','heres','hers','herself','him','himself','his','how','hows','i','id','ill','im','ive','if','in','into','is','isnt','it','its','itself','lets','me','more','most','mustnt','my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours','ourselves','out','over','own','same','shant','she','shed','shell','shes','should','shouldnt','so','some','such','than','that','thats','the','their','theirs','them','themselves','then','there','theres','these','they','theyd','theyll','theyre','theyve','this','those','through','to','too','under','until','up','very','was','wasnt','we','wed','well','were','weve','were','werent','what','whats','when','whens','where','wheres','which','while','who','whos','whom','why','whys','with','wont','would','wouldnt','you','youd','youll','youre','youve','your','yours','yourself','yourselves']
#online_stop = ['a','about','above','after','all','am','an','and','any','are','arent','as','at','be','because','been','before','being','below','between','both','but','by','did','didnt','do','does','doesnt','doing','dont','down','during','each','few','for','from','further','had','hadnt','has','hasnt','have','havent','having','he','hed','hes','her','here','heres','hers','herself','him','himself','his','how','hows','i','id','ill','im','ive','if','in','into','is','isnt','it','its','itself','lets','me','more','my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours','ourselves','out','over','own','same','shant','she','shed','shell','shes','should','so','some','such','than','that','thats','the','their','theirs','them','themselves','then','there','theres','these','they','theyd','theyll','theyre','theyve','this','those','through','to','too','under','until','up','very','was','wasnt','we','wed','well','were','weve','were','werent','what','whats','when','whens','where','wheres','which','while','who','whos','whom','why','whys','with','wont','would','wouldnt','you','youd','youll','youre','youve','your','yours','yourself','yourselves']
#online_stop = ['i','a','not','about','an','are','and','if ','so','as','at','be','by','com','de','en','for','from','how','in','is','it','la','of','on','or','that','the','this','to','was','what','when','where','who','will','with','und','the','and','but','its']
online_stop = ['a', 'able', 'about', 'above', 'abroad', 'abst', 'accordance', 'according', 'accordingly', 'across', 'act', 'actually', 'added', 'adj', 'adopted', 'affected', 'affecting', 'affects', 'after', 'afterwards', 'again', 'against', 'ago', 'ah', 'ahead', 'aint', 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'alongside', 'already', 'also', 'although', 'always', 'am', 'amid', 'amidst', 'among', 'amongst', 'amoungst', 'amount', 'an', 'and', 'announce', 'another', 'any', 'anybody', 'anyhow', 'anymore', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'apparently', 'appear', 'appreciate', 'appropriate', 'approximately', 'are', 'aren', 'arent', 'arise', 'around', 'as', 'aside', 'ask', 'asking', 'associated', 'at', 'auth', 'available', 'away', 'awfully', 'b', 'back', 'backward', 'backwards', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'begin', 'beginning', 'beginnings', 'begins', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'bill', 'biol', 'both', 'bottom', 'brief', 'briefly', 'but', 'by', 'c', 'ca', 'call', 'came', 'can', 'cannot', 'cant', 'caption', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly', 'cmon', 'co', 'co.', 'com', 'come', 'comes', 'computer', 'con', 'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', 'couldnt', 'course', 'cry', 'cs', 'currently', 'd', 'dare', 'darent', 'date', 'de', 'definitely', 'describe', 'described', 'despite', 'detail', 'did', 'didnt', 'different', 'directly', 'do', 'does', 'doesnt', 'doing', 'done', 'dont', 'down', 'downwards', 'due', 'during', 'e', 'each', 'ed', 'edu', 'effect', 'eg', 'eight', 'eighty', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'end', 'ending', 'enough', 'entirely', 'especially', 'et', 'et-al', 'etc', 'even', 'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'f', 'fairly', 'far', 'farther', 'few', 'fewer', 'ff', 'fifteen', 'fifth', 'fify', 'fill', 'find', 'fire', 'first', 'five', 'fix', 'followed', 'following', 'follows', 'for', 'forever', 'former', 'formerly', 'forth', 'forty', 'forward', 'found', 'four', 'from', 'front', 'full', 'further', 'furthermore', 'g', 'gave', 'get', 'gets', 'getting', 'give', 'given', 'gives', 'giving', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'greetings', 'h', 'had', 'hadnt', 'half', 'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he', 'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herse', 'herself', 'hes', 'hi', 'hid', 'him', 'himse', 'himself', 'his', 'hither', 'home', 'hopefully', 'how', 'howbeit', 'however', 'hows', 'hundred', 'i', 'id', 'ie', 'if', 'ignored', 'ill', 'im', 'immediate', 'immediately', 'importance', 'important', 'in', 'inasmuch', 'inc', 'inc.', 'indeed', 'index', 'indicate', 'indicated', 'indicates', 'information', 'inner', 'inside', 'insofar', 'instead', 'interest', 'into', 'invention', 'inward', 'is', 'isnt', 'it', 'itd', 'itll', 'its', 'itse', 'itself', 'ive', 'j', 'just', 'k', 'keep', 'keeps', 'kept', 'keys', 'kg', 'km', 'know', 'known', 'knows', 'l', 'largely', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'likewise', 'line', 'little', 'll', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'm', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'maynt', 'me', 'mean', 'means', 'meantime', 'meanwhile', 'merely', 'mg', 'might', 'mightnt', 'mill', 'million', 'mine', 'minus', 'miss', 'ml', 'more', 'moreover', 'most', 'mostly', 'move', 'mr', 'mrs', 'much', 'mug', 'must', 'mustnt', 'my', 'myse', 'myself', 'n', 'na', 'name', 'namely', 'nay', 'nd', 'near', 'nearly', 'necessarily', 'necessary', 'need', 'neednt', 'needs', 'neither', 'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'no', 'no-one', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'nor', 'normally', 'nos', 'not', 'noted', 'nothing', 'notwithstanding', 'novel', 'now', 'nowhere', 'o', 'obtain', 'obtained', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'omitted', 'on', 'once', 'one', 'ones', 'only', 'onto', 'opposite', 'or', 'ord', 'other', 'others', 'otherwise', 'ought', 'oughtnt', 'our', 'ours', 'ours ', 'ourselves', 'out', 'outside', 'over', 'overall', 'owing', 'own', 'p', 'page', 'pages', 'part', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'poorly', 'possible', 'possibly', 'potentially', 'pp', 'predominantly', 'present', 'presumably', 'previously', 'primarily', 'probably', 'promptly', 'proud', 'provided', 'provides', 'put', 'q', 'que', 'quickly', 'quite', 'qv', 'r', 'ran', 'rather', 'rd', 're', 'readily', 'really', 'reasonably', 'recent', 'recently', 'ref', 'refs', 'regarding', 'regardless', 'regards', 'related', 'relatively', 'research', 'respectively', 'resulted', 'resulting', 'results', 'right', 'round', 'run', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'sec', 'second', 'secondly', 'section', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven', 'several', 'shall', 'shant', 'she', 'shed', 'shell', 'shes', 'should', 'shouldnt', 'show', 'showed', 'shown', 'showns', 'shows', 'side', 'significant', 'significantly', 'similar', 'similarly', 'since', 'sincere', 'six', 'sixty', 'slightly', 'so', 'some', 'somebody', 'someday', 'somehow', 'someone', 'somethan', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specifically', 'specified', 'specify', 'specifying', 'state', 'states', 'still', 'stop', 'strongly', 'sub', 'substantially', 'successfully', 'such', 'sufficiently', 'suggest', 'sup', 'sure', 'system', 't', 'take', 'taken', 'taking', 'tell', 'ten', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', 'thatll', 'thats', 'thatve', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'thered', 'therefore', 'therein', 'therell', 'thereof', 'therere', 'theres', 'thereto', 'thereupon', 'thereve', 'these', 'they', 'theyd', 'theyll', 'theyre', 'theyve', 'thick', 'thin', 'thing', 'things', 'think', 'third', 'thirty', 'this', 'thorough', 'thoroughly', 'those', 'thou', 'though', 'thoughh', 'thousand', 'three', 'throug', 'through', 'throughout', 'thru', 'thus', 'til', 'till', 'tip', 'to', 'together', 'too', 'took', 'top', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'ts', 'twelve', 'twenty', 'twice', 'two', 'u', 'un', 'under', 'underneath', 'undoing', 'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'ups', 'upwards', 'us', 'use', 'used', 'useful', 'usefully', 'usefulness', 'uses', 'using', 'usually', 'uucp', 'v', 'value', 'various', 've', 'versus', 'very', 'via', 'viz', 'vol', 'vols', 'vs', 'w', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome', 'well', 'went', 'were', 'werent', 'weve', 'what', 'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever', 'whens', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres', 'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while', 'whilst', 'whim', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl', 'whom', 'whomever', 'whos', 'whose', 'why', 'whys', 'widely', 'will', 'willing', 'wish', 'with', 'within', 'without', 'wonder', 'wont', 'words', 'world', 'would', 'wouldnt', 'www', 'x', 'y', 'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre', 'yours', 'yourself', 'yourselves', 'youve', 'z', 'zero']
#online_stop.extend(['a', 'about', 'above', 'across', 'after', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'among', 'an', 'and', 'another', 'any', 'anybody', 'anyone', 'anything', 'anywhere', 'are', 'area', 'areas', 'around', 'as', 'ask', 'asked', 'asking', 'asks', 'at', 'away', 'b', 'back', 'backed', 'backing', 'backs', 'be', 'became', 'because', 'become', 'becomes', 'been', 'before', 'began', 'behind', 'being', 'beings', 'best', 'better', 'between', 'big', 'both', 'but', 'by', 'c', 'came', 'can', 'cannot', 'case', 'cases', 'certain', 'certainly', 'clear', 'clearly', 'come', 'could', 'd', 'did', 'differ', 'different', 'differently', 'do', 'does', 'done', 'down', 'downed', 'downing', 'downs', 'during', 'e', 'each', 'early', 'either', 'end', 'ended', 'ending', 'ends', 'enough', 'even', 'evenly', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'f', 'face', 'faces', 'fact', 'facts', 'far', 'felt', 'few', 'find', 'finds', 'first', 'for', 'four', 'from', 'full', 'fully', 'further', 'furthered', 'furthering', 'furthers', 'g', 'gave', 'general', 'generally', 'get', 'gets', 'give', 'given', 'gives', 'go', 'going', 'good', 'goods', 'got', 'great', 'greater', 'greatest', 'group', 'grouped', 'grouping', 'groups', 'h', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'herself', 'high', 'higher', 'highest', 'him', 'himself', 'his', 'how', 'however', 'i', 'if', 'important', 'in', 'interest', 'interested', 'interesting', 'interests', 'into', 'is', 'it', 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kind', 'knew', 'know', 'known', 'knows', 'l', 'large', 'largely', 'last', 'later', 'latest', 'least', 'less', 'let', 'lets', 'like', 'likely', 'long', 'longer', 'longest', 'm', 'made', 'make', 'making', 'man', 'many', 'may', 'me', 'member', 'members', 'men', 'might', 'more', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', 'my', 'myself', 'n', 'necessary', 'need', 'needed', 'needing', 'needs', 'never', 'new', 'newer', 'newest', 'next', 'no', 'nobody', 'non', 'noone', 'not', 'nothing', 'now', 'nowhere', 'number', 'numbers', 'o', 'of', 'off', 'often', 'old', 'older', 'oldest', 'on', 'once', 'one', 'only', 'open', 'opened', 'opening', 'opens', 'or', 'order', 'ordered', 'ordering', 'orders', 'other', 'others', 'our', 'out', 'over', 'p', 'part', 'parted', 'parting', 'parts', 'per', 'perhaps', 'place', 'places', 'point', 'pointed', 'pointing', 'points', 'possible', 'present', 'presented', 'presenting', 'presents', 'problem', 'problems', 'put', 'puts', 'q', 'quite', 'r', 'rather', 'really', 'right', 'room', 'rooms', 's', 'said', 'same', 'saw', 'say', 'says', 'second', 'seconds', 'see', 'seem', 'seemed', 'seeming', 'seems', 'sees', 'several', 'shall', 'she', 'should', 'show', 'showed', 'showing', 'shows', 'side', 'sides', 'since', 'small', 'smaller', 'smallest', 'so', 'some', 'somebody', 'someone', 'something', 'somewhere', 'state', 'states', 'still', 'such', 'sure', 't', 'take', 'taken', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'therefore', 'these', 'they', 'thing', 'things', 'think', 'thinks', 'this', 'those', 'though', 'thought', 'thoughts', 'three', 'through', 'thus', 'to', 'today', 'together', 'too', 'took', 'toward', 'turn', 'turned', 'turning', 'turns', 'two', 'u', 'under', 'until', 'up', 'upon', 'us', 'use', 'used', 'uses', 'v', 'very', 'w', 'want', 'wanted', 'wanting', 'wants', 'was', 'way', 'ways', 'we', 'well', 'wells', 'went', 'were', 'what', 'when', 'where', 'whether', 'which', 'while', 'who', 'whole', 'whose', 'why', 'will', 'with', 'within', 'without', 'work', 'worked', 'working', 'works', 'would', 'x', 'y', 'year', 'years', 'yet', 'you', 'young', 'younger', 'youngest', 'your', 'yours', 'z'])
#stop_words.extend(single_char)
stop_words.extend(online_stop)
stop_words = list(set(stop_words))
#stop_words.sort()
#stop_words = []

fn = sys.argv[1]
word_dict = {}
prefix_hash = {}
word_prob_log = {}
prior_prob_log = {}

all_t_files=[]
all_d_files=[]
all_n_files=[]
all_p_files=[]

def transform(temp):
    if temp == "imo":
        return "opinion"
    elif temp == "inches":
        return "inch"
    elif temp == "including" or temp == "included" or temp == "includes":
        return "include"
    elif temp == "issued" or temp == "issues":
        return "issue"
    elif temp == "ppl":
        return "people"
    elif temp == "prices":
        return "price"
    elif temp == "say":
        return "says"
    elif temp == "shocked" or temp == "shocker" or temp == "shocking":
        return "shock"
    #elif temp == "sooooo" or temp == "soooo" or temp == "sooo" or temp == "soo":
    #    return "so"
    return temp


def setClassPaths(fn):
    tempList = []
    for root, dir, files in os.walk(fn):
            for items in fnmatch.filter(files, "*.txt"):
                    temp = root+"/"+items
                    temp1 = temp
                    if "readme" not in temp1.lower():
                        tempList.append(temp)
    return tempList



def getPureWord(w):
    temp = w.lower()
    #number and word
    #print ''.join(e for e in temp if e.isalnum())        
    temp = ''.join(e for e in temp if e.isalpha()) 
    if temp not in stop_words and temp !='':
        return transform(temp)
    else:
        return ""

def getClassLogScore(l):
    sum = {}
    #print prefix_hash.keys()
    return sum

def getClassLogScore1(l):
    sum = {}
    for key in prefix_hash.keys():
        sum[key]=0.0
        sum[key]+=prior_prob_log.get(key)
        for word in l.split():
            temp = getPureWord(word)
            temp1 = prefix_hash.get(key)+temp
            sum[key]+=word_prob_log.get(temp1,0)
    return sum

def getFilenames(beginPath,classPaths):
    tempArr = []
    for path in classPaths:
        for fold in folds:
            fullpath = beginPath+path+fold
            onlyfiles = [fullpath+f for f in listdir(fullpath) if isfile(join(fullpath, f))]
            tempArr.extend(onlyfiles)
    return tempArr


def init(fn):
    f = open("nbmodel.txt", "r")
    for line in f:
        words = line.split()
        if "patro_patro_" in words[0]:
            temp = words[0].replace("patro_patro_","")
            prior_prob_log[temp] = float(words[1])
        else:
            word_prob_log[words[0]] = float(words[1])
    f.close()

def maxDictVal(d,listings):
    maxKey = listings[0]
    for key in listings:
        if d[key] > d[maxKey]:
            maxKey = key
    return maxKey

def writeVal(fh,line,fileElt):
    val = {}
    val = getClassLogScore1(line)
    #print val

    #temp = maxDictVal(val,["positive","negative"]) + " " +maxDictVal(val,["truthful","deceptive"]) + " " + fileElt
    
    c1 = ["negative","positive"]
    c2 = ["deceptive","truthful"]
    t1 = "positive"
    t2 = "deceptive"
    if "negative_polarity" in fileElt:
        t1 = "negative"
    if "truthful_from_" in fileElt:
        t2 = "truthful"
    i1 = maxDictVal(val,c1)
    i2 = maxDictVal(val,c2)
    #temp = i2 + "," + i1 + "," + t2 + "," + t1+","+fileElt
    temp = i2 + " " + i1 + " " + fileElt
    #print temp

    #if t1 == i1:
    #    if t1 == "positive":
    #        true_pos_pos+=1
    #    else:
    #        true_pos_neg+=1
    #else:
    #    if t1 == "positive":
    #        false_neg_pos+=1
    #        false_pos_neg+=1
    #    else:
    #        false_neg_neg+=1
    #        false_pos_pos+=1
    #
    #if t1 == i2:
    #    if t1 == "truthful":
    #        true_pos_truth+=1
    #    else:
    #        true_pos_decep+=1
    #else:
    #    if t1 == "truthful":
    #        false_neg_truth+=1
    #        false_pos_decep+=1
    #    else:
    #        false_neg_decep+=1
    #        false_pos_truth+=1



    fp.write(temp)
    fp.write("\n")


def predict2Class(fh,fileList):
    for fileElt in fileList:
        fr = open(fileElt, "r")
        for line in fr:
            writeVal(fh,line,fileElt)

def merge(a,b,c,d):
    op = a
    for i in b:
        if i not in op:
            op.append(i)
    for i in c:
        if i not in op:
            op.append(i)
    for i in d:
        if i not in op:
            op.append(i)
    #print op
    #print len(op)
    return op

if os.path.exists(fn):
    prefix_hash["positive"]  = "p_"
    prefix_hash["negative"]  = "n_"
    prefix_hash["truthful"]  = "t_"
    prefix_hash["deceptive"] = "d_"
    true_pos_pos = 0
    true_pos_neg = 0
    true_pos_truth = 0
    true_pos_decep = 0

    false_pos_pos = 0
    false_pos_neg = 0
    false_pos_truth = 0
    false_pos_decep = 0

    false_neg_pos = 0
    false_neg_neg = 0
    false_neg_truth = 0
    false_neg_decep = 0


    init(fn)



    merge_files=setClassPaths(fn)
    #all_t_files.extend(getFilenames(fn,true_end))
    #all_d_files.extend(getFilenames(fn,deceptive_end))
    #all_n_files.extend(getFilenames(fn,negative_end))
    #all_p_files.extend(getFilenames(fn,positive_end))

    fp = open("nboutput.txt","w")
    #print word_prob_log
    #print len(word_prob_log)
    #print "gunu"
    #print prior_prob_log
    
    #merge_files = merge(all_t_files,all_d_files,all_p_files,all_n_files)


    #predict2Class(fp,all_p_files)
    #predict2Class(fp,all_n_files)
    #predict2Class(fp,all_t_files)
    #predict2Class(fp,all_d_files)
    predict2Class(fp,merge_files)
    #s1 = str()
    fp.close()
    #getScores(c1,c2)
    #print getClassLogScore(prior_prob_log.get("positive"),"England Caribbean United1")
else:
    print "File does not exists"

