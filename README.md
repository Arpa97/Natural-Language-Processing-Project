# Reccomender di contenuti basato su NLP

- Corso di Natural Language Processing
- Laurea Magistrale in informatica Università di Bologna
- Anno accademico 2022/23

Realizzato da:

- D'Arpa, Andrea, 0000983830


Il codice è rilasciato sotto licenza GPL 3.0

![](https://www.gnu.org/graphics/gplv3-or-later.png)
https://www.gnu.org/licenses/gpl-3.0.md

## Introduzione
### Descrizione del problema
Le piattaforme di streaming sono oggi il mezzo più diffuso per consumare film, serie tv e contenuti audiovisivi amatoriali. Netflix, Amazon Prime Video, Youtube, Disney+; tutte queste piattaforme hanno una cosa in comune: un algoritmo di raccomandazione dei video.
Tale algoritmo serve a consigliare in maniera automatica i contenuti che più potrebbero interessare ad un utente; impresa non facile, considerato la mole di contenuti ospitati sulle attuali piattaforme e la difficoltà nel definire con precision piace ad un utente, definizione spesso oscura anche all'utente stesso.

Il problema si delinea quindi nel selezionare un sottoinsieme di titoli, dall'enorme insieme composto dai titoli disponibili, che 
possono ineressare e piacere alll'utente in modo da rendere più facile la navigazione nella libreria a disposizione e la scelta del prossimo contenuto da vedere.


### Descrizione della soluzione proposta
In questo progetto mi sono concentrato sulle tecniche di filtrazione basate su contenuti; in particolar modo su tecniche di analisi del linguaggio naturale delle descrizioni testuali della trama dei film o delle serie e dei metadati correlati ad essi.

Nello specifico vengono usati dei modelli a conta per estrarre i vettori semantici dalle descrizioni e dai metadati, confrontando poi il vettore ottenuto dai contenuti visualizzati e piaciuti all'utente con i vettori dei contenuti presenti nella libreria, consigliando poi quelli con una similarità maggiore.
Per confontare i vettori si calcola la coseno-similarità tra gli stessi, valore compreso tra zero e uno, a valori maggiori corrisponde una maggior somiglianza tra i vettori e quindi tra i contenuti corrispondenti.

### Revisione della letteratura
L'Approccio al problema storicamente è cambiato nel tempo, e da algoritmi semplici, si è passato all'analisi dei grafi su web semantico, fino ad arrivare oggi all'implementazione di intelligenze artificiali in grado di comprendere i contenuti che potrebbero interessare un utente.
Interessati da questo problema, mi sono cimentato nell'implementare un reccomender basato su Machine Learning in Python.
Ci sono principalmente tre tecniche utilizzate:

 - **Filtro demografico**: Le raccomandazioni sono le stesse per ogni utente. Sono generiche e non personalizzate
 - **Filtro basato su contenuti**: Si utilizzano i metadati dei contenuti consumati dall'utente. L'idea di base è: se un utente ha apprezzato un contenuto, allora dovrà apprezzare contenuti simili.
 - **Filtro Collaborativo**: Si prende in considerazione l'utente come se fosse un oggetto. Si cercano di accomunare più utenti con gusti simili, e vengono consigliati i contenuti consumati da un utente nel gruppo a tutti gli altri che non hanno ancora fruito di quest'ultimo.

### Presentazione dei risultati ottenuti
Per presentare i risultati ottenuti andremo ad analizzare un ciclo di esecuzione del software:
Andiamo a vedere i risultati per il celebre e conosciuto film UP (Disney Pixar).

Andiamo ad analizzare la correttezza dei risultati. Le trame e i dati in questa documentazione sono presi da TMDB in italiano. Sono le traduzioni ufficiali delle trame (in inglese) che troviamo nel dataset usato per calcolare i vettori di caratteri.

#### Raccomandazioni con analisi della trama:
##### Input:
- Up: In una sala cinematografica si proietta un cinegiornale su un esploratore, Charles Muntz, che è tornato dall'America del Sud con lo scheletro di un uccello che la scienza ufficiale qualifica come falso. Muntz riparte per dimostrare la sua onestà. Un bambino occhialuto, Carl, è in sala. Muntz è il suo eroe. Incontrerà una bambina, Ellie, che ha la sua stessa passione. I due cresceranno insieme e si sposeranno. Un giorno però Carl si ritrova vedovo con la sua villetta circondata da un cantiere e con il sogno che i contrattempi della vita non hanno mai permesso a lui ed Ellie di realizzare: una casa in prossimità delle cascate citate da Muntz come luogo della sua scoperta. Un giorno un Giovane Esploratore bussa alla sua porta. Sarà con lui che Carl, senza volerlo, comincerà a realizzare il sogno.

##### Consigliati:
- Raising Helen: Helen Harris sta vivendo un sogno: la sua agenzia di modelle è in ascesa e la sua carriera al top. Ma quando dopo la tragica morte della sorella e del cognato, Helen si trova costretta ad accudire i tre nipotini, le cose sembrano destinate a cambiare.

- Steven Russell conduce una vita piuttosto ordinaria: è un agente di polizia, suona l'organo nella chiesa del paese, è felicemente sposato con Debbie. Fino a quando un grave incidente d'auto non gli fa aprire gli occhi: è gay e desidera vivere la sua vita al massimo, anche a costo di infrangere la legge. Iniziando a vivere la sua nuova vita stravagante, Steven non esiterà ad imbrogliare chiunque per sbarcare il lunario, e alla fine verrà spedito al Penitenziario di Stato dove incontrerà l'amore della sua vita, un uomo sensibile e dai modi gentili che si chiama Phillip Morris. La sua determinazione a far uscire Phillip di prigione e a costruire una vita perfetta insieme, lo spingeranno a tentare, con successo, un colpo impossibile dopo l'altro.

- I cavalli sono l'anima e il sangue della storia. Siamo negli anni quaranta. Il cow boy John Grady Cole (Demon, appunto) vede letteralmente capovolgersi il suo mondo. Ciò che resta del west viene ingoiato dalle strade e dalle costruzioni. Il colpo di grazia glielo dà sua madre, che vende il ranch a una società petrolifera. Partendo per il Messico col suo amico Lacey, Cole crede di trovare qualcosa di ciò che ha perduto, una terra selvaggia buona anche per i cavalli. In principio le cose sembrano funzionare, il cow boy trova ranch, lavoro e anche l'amore. Ma la ragazza non è quella giusta, infatti è la figlia del padrone, e laggiù nel Messico non basta essere innamorati per essere felici. Tutt'altro. E così John comincia a "perdere". Prima gli appioppano una falsa accusa di omicidio, poi, il padre della ragazza fa di tutto per separare i due, ad ogni costo.

- Dancer in the Dark: E' il 1964, Selma è emigrata con suo figlio dall'Europa dell'Est in America. Lavora notte e giorno per salvare suo figlio dalla stessa malattia che affligge lei e che la renderà cieca. Il segreto della sua energia di vivere è il suo amore per i musical. Quando la vita è troppo dura, le basta fingere di trovarsi nel meraviglioso mondo dei musical, dove riesce a trovare la felicità che il mondo non le riesce a dare.

- An Education: Londra, anni '60. Quando nella vita di Jenny, diciassettenne determinata al successo negli studi, arriva David, un playboy che ha il doppio dei suoi anni, le sue prospettive cambiano radicalmente...

#### Le raccomandazioni in output analizzando i metadati dei film invece sono:

##### input:
- UP: Animazione, Commedia, Famiglia, Avventura

##### output:

- Monsters, Inc.: Animazione, Commedia, Famiglia

- Meet the Deedles: Commedia, Famiglia

- Alpha and Omega: The Legend of the Saw Tooth Cave : Famiglia, Animazione, Commedia, Avventura

- Elsa & Fred: Commedia, Romance, Dramma

- The Nut Job: Animazione, Commedia, Famiglia, Avventura



#### Altre raccomandazioni
È inoltre possibile inserire nel sistema molteplici film. In quel caso verrà fatta una media di punti in comune tra le trame e verranno calcolati dei risultati che hanno maggior pertinenza con il maggior numero di elementi in comune tra i film (sia per trama che per metadati).
Per non dilungarci troppo, lascio riportati qui due esempi di output con lo stesso input, senza però lasciare trame o metadati, lasciando al lettore il compito di approfondire nel caso lo ritenesse interessante (o non conoscesse i titoli di cui si parla).

##### Film in input
- Harry Potter and the half bloody prince
- Avenger: Age of Ultron
- Pirates of the Caribbean: At World's End

##### Film in output (trama)
- Harry Potter and the Goblet of Fire
- Harry Potter and the Order of the Phoenix
- The Avengers
- My Stepmother Is an Alien
- Harry Potter and the Prisoner of Azkaban

##### Film in output (meta)
- Pirates of the Caribbean: Dead Man's Chest
- Harry Potter and the Philosopher's Stone
- Pirates of the Caribbean: The Curse of the Black Pearl
- Harry Potter and the Chamber of Secrets
- Harry Potter and the Order of the Phoenix


### Metodo proposto
L' algoritmo si sviluppa prevalentemente in 2 fasi:

 1. Analisi dei dati:
	 - Si  effettua l'analisi dei dati usando tecniche di Exploratory Data Analysis (EDA)
 2. Si costruisce il sistema di raccomandazione e si stampano i risultati ottenuti

#### Analisi dei dati
Il modello usato è fornito dalla libreria "scikitlearn" ed è pre-trainato utilizzando training non supervisionato sul dataset di Wikipedia in inglese con tecniche di Clustering Partizionale.

Il dataset usato è formato da due file .csv: credits (che contiene tutti i metadati sul film) e movies (che contiene informazioni come nome, id, budget, lingue, ...)

Per caricare i dataset è stata utilizzata la libreria [pandas](https://pandas.pydata.org/),  un veloce, semplice, flessibile nonché potente sistema di analisi e manipolazione dei dati open source e scritto in python.

Ovviamente i dataset contengono molti più dati e informazioni di quante ne servano realmente. Dunque, sono stati applicati dei filtri ed è stata creata un'unica matrice contenente i dati interessanti.

    credits.columns = ['id','title','cast','crew']
    movies = movies.merge(credits, on="id")
    
Una volta ottenuta la nostra matrice contenente le informazioni di cui sopra, andiamo a formattare i nostri dati legandoli ai tipi di dati corretti:
cast, crew, keyword, director e genere.
Quindi andiamo a creare una "zuppa", ovvero una rappresentazione navigabile dei dati.

A questo punto creiamo la matrice dei termini andando ad analizzare il dizionario dei vocaboli nel nostro dataset e calcoliamo la coseno similarità tra le varie entry della nostra matrice
	
	count_vectorizer = CountVectorizer(stop_words="english")
	count_matrix = count_vectorizer.fit_transform(movies["soup"])
	cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

A questo punto possiamo vedere le similarità dei campi, andando ad annalizzare i metadati del film. Il metodo appena raccontato si occupa di ritornare il nostro "metro di paragone" per l'accuratezza del nostro metodo di analisi delle trame.

A questo punto andiamo a creare (tramite la libreria sklearn) il nostro TfidfVectorizer.
Il TfidfVectorizer non è altro che un "vettorizzatore" che applica la funzione di peso tf-idf (term frequency–inverse document frequency), una funzione utilizzata in information retrieval per misurare l'importanza di un termine rispetto ad un documento o ad una collezione di documenti. Questa aumenta proporzionalmente al numero di volte che il termine è contenuto nel documento, ma cresce in maniera inversamente proporzionale con la frequenza del termine nella collezione. L'idea alla base di questo comportamento è di dare più importanza ai termini che compaiono nel documento, ma che in generale sono poco frequenti.

	tfidf = TfidfVectorizer(stop_words="english")
	movies["overview"] = movies["overview"].fillna("")
	tfidf_matrix = tfidf.fit_transform(movies["overview"])
	cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

Il Vettorizatore, a differenza del metodo precedente, prende solo il campo "overview" della matrice, ovvero il campo contenente la trama in inglese.
Dopo la vettorizzazione, anche in questo caso si è calcolata la coseno similarità per la matrice tfidf.

#### Il reccomender
Una volta manipolati i dati, si può passare alla costruzione effettiva del sistema di raccomandazione.


La funzione get_recommendations()  prende il titolo del film e le matrici di similarità come input. Segue i passaggi qui sotto spiegati per fare delle raccomandazioni:
-   Ottiene l'indice del film utilizzando il suo titolo.
- Ottiene una lista di punteggi di similarità con il film scelto rispetto a tutti i film
-  Crea delle tuple con il primo elemento come indice e il secondo il punteggio di coseno-similarità
-  Ordina la lista di tuple in ordine discendente basandosi sul punteggio di similarità
- Ottiene l'indice della top 10 film dalla lista appena ordinata, escludendo il primo titolo che è il film scelto per la comparazione
- Mappa gli indici ai rispettivi titoli, e ritorna una lista di film

.

	idx = indices[title]
	similarity_scores = list(enumerate(cosine_sim[idx]))
	similarity_scores= sorted(similarity_scores, key=lambda x: x[1], reverse=True)
	similarity_scores= similarity_scores[1:11]
	# (a, b) where a is id of movie, b is similarity_scores
	movies_indices = [ind[0] for ind in similarity_scores]
	moviesT = movies["id"].iloc[movies_indices]
	return moviesT

### Ricerca della soluzione
Ho analizzato più tecniche di filtro di contenuti e preso in considerazione prevalentemente due aree ben diverse:
- Content-Based Recommender Systems
- Collaborative Filtering Recommender Systems

I recommender basati su contenuti analizzano le preferenze dell'utente per trovare corrispondenze con i vari oggetti disponibili nell'insieme dei vari contenuti/dati da raccomandare. Ad esempio, un e-commerce avrà un sistema di raccomandazioni che fornirà degli articoli correlati a quelli presenti nello storico di ricerche di un utente, alle recenzioni lasciate e agli oggetti comprati.
Per fare ciò vengono codificate le informazioni di ogni oggetto in un vettore, e utilizzando delle semplici metriche di similarità come la coseno similarità o la distanza euclidea, possiamo capire quanto simili (allineati) siano due vettori

I reccomender basati su filtraggio collaborativo invece non necessitano informazioni sugli oggetti che consigliano. Le raccomandazioni sono proposte in base alla similarità tra utenti.
Ad esempio, se un sistema di raccomandazione basato su filtraggio collaborativo conosce che l'utente A e l'utente B hanno gusti simili in fatto di scarpe, assumerà che avranno gusti simili anche in futuro. Come risultato, se l'utente A compra un paio di scarpe, il sistema le raccomanderà all'utente B.
 

### Giustificazione della scelta
Il vantaggio principale dei sistemi basati su contenuti è quello di poter creare dei modelli di dominio espliciti. Il creatore del sistema può utilizzare i dati sul prodotto. In questo modo si può utilizzare da subito in modo efficace, senza aver bisogno di una larga user base per fare delle raccomandazioni adeguate.

Al contrario, i sistemi a filtraggio collaborativo hanno bisogno di molti dati utente per poter fare raccomandazioni. Infatti si presenta il problema della partenza a rilento, dove il sistema impiega del tempo per un nuovo utente a fare delle raccomandazioni interessanti o pertinenti.
È basato su principi semplici, è molto adattabile ed è una delle tecniche che hanno letteralmente rivoluzionato il mondo delle raccomandazioni.
Possono tuttavia fare raccomandazioni basate solo su un tipo di contenuti, dunque nel caso dell'esempio dell'e-commerce sarebbe limitato nell'abilità di fare raccomandazioni su oggetti al difuori dei prodotti appartenenti al suo dataset.

Dunque, principalmente per motivi legati all'immediatezza di riscontro, ho scelto di utilizzare dei sistemi basati su contenuti. In questo modo, una piattaforma può fornire dei buoni risultati immediatamente, senza dover attendere che l'utente prosegua nell'utilizzo per un primo periodo prima di poter avere delle raccomandazioni.


## Risultati sperimentali

### Elenco delle tecnologie usate per gli esperimenti
Il caso da noi preso in considerazione necessita di un'analisi umana per stimare la qualità dei risultati.
Ho dunque utilizzato dei semplici fogli di calcolo dove, dopo aver sottoposto a più persone la lista di correlazioni, fatto una media dei voti sui singoli risultati, per poi calcolare una media totale sui risultati utilizzando le funzioni di media.
Ho poi utilizzato Python per ottenere risultati da altri algoritmi, sottoponendoli allo stesso trattamento per poter trarre conclusioni sulle differenze tra il mio metodo, e quelli già presenti in letteratura.

### Descrizione del metodo per la misurazione delle performance
Per valutare le performance del sistema ho utilizzato la precisione seguendo la formula:

***Precision = Consigliati Rilevanti/Consigliati***

Ovvero il rapporto tra i titoli consigliati pertinenti rispetto ai titoli di partenza ed il totale dei titoli consigliati dal sistema.
Per effettuare la misurazione i titoli rilevanti sono stati indicati caso per caso da un operatore.

### Risultati della configurazione migliore

### Studio di ablazione
Ho realizzato due diversi modelli per l'ottenimento dei dati da analizzare: 
Il primo modello prendeva in input un titolo casuale dalla lista, ritornando 10 risultati, il secondo invece prendeva in input 5 film casuali dalla lista, ritornando sempre 10 risultati.
Ho assegnato un valore da 0 a 10 per pertinenza di correlazione tra i titoli dei film in input rispetto ai titoli dei film ritornati dal programma. Questa analisi è stata portata avanti sia per i risultati ritornati dall'analisi della similarità di trama, che dall'analisi dei risultati per similarità di metadati.
I risultati sono osservabili nella tabella presente nel file *valutazione_precisione.xslx* nella root del repository.

### Studio di comparazione
Ho dunque proceduto ad analizzare le differenze tra il mio metodo e il metodo illustrato in [Distributed Representations of Sentences and Documents](http://proceedings.mlr.press/v32/le14.html?ref=https://githubhelp.com) (da ora DRSD).
Lo studio è osservabile nel documento *valutazione_neural_network.xlsx* nella root del repository.
L'algoritmo preso da DRSD restituisce i risultati analizzando i testi delle trame.

| TRAMA_ANDREA    | METADATI_ANDREA| TRAMA_DRSD          |
|---------------------|-------------------|---------------------|
| 60.8% input singolo | 71% input singolo | 22.6% input singolo |
| 66.2% 5 input       | 67.2% 5 input     | 33.8% 5 input       |

Come si può osservare, i risultati del mio algoritmo sono sensibilmente più precisi.

## Discussione e conclusioni

### Discussione dei risultati ottenuti
Ho utilizzato Python 3, utilizzando delle librerie utili allo scopo, quali SciKitLearn, Pandas e NumPy. Nello specifico:
- SciKitLearn per ottenere vettorializzare le stringhe delle descrizioni (contenute all'interno dei nostri file CSV presi da TheMovieDataBase.org)
- Pandas per gestire i dati in input
- NumPy per la parte di calcolo sui vettori, come ad esempio il calcolo della distanza di editing 

### Il metodo proposto rispetta le attese? 
Il metodo proposto riesce correttamente a proporre (con un leggero margine di errore) dei film coerenti con quello/i inseriti. 

Se questo risultato risulta più "scontato" con l'analisi dei metadati del film (come genere, cast e direzione), lo stesso non si può dire dell'analisi della trama. Tuttavia si è riscontrato come, in quest'ultimo caso, il recommender faccia egregiamente il suo lavoro, andando a consigliare film che hanno caratteristiche peculiari a livello di trama con quello/i inserito/i dall'utente, senza riguardi per genere o cast, trovando dunque dei suggerimenti meno scontati e interessanti.

### Limite del metodo
Il metodo proposto ha difficoltà nel diversificare i contenuti consigliati. Andando ad elaborare la similarità su tutto il dataset, infatti, abbiamo le stesse raccomandazioni per ogni contenuto dato in input. Inoltre il calcolo della similarità impiega più tempo rispetto all'operare su un dataset ristretto.

### Lavori futuri
Per terminare il lavoro, può essere interessante implementare un algoritmo di filtro collaborativo, in modo da utilizzare entrambe le tecniche al fine di raffinare i contenuti consigliati all'utente. 
Al posto dunque di calcolare la coseno similarità con un item su tutto il dataset, si andrebbe così a implementare il metodo di content based filtering sul set di oggetti provenienti dallo storico di utenti con gusti simili. In questo modo si potrebbero consigliare film o serie tv scelte da altri utenti che hanno apprezzato i nostri stessi contenuti con elevata attinenza a ciò che è stato consumato dall'utente in questo momento, con diversificazione dei suggerimenti sia tra utenti differenti, che nel tempo per lo stesso utente. Inoltre, andando ad elaborare i dati su un sottoinsieme di dati, avremmo un calcolo più rapido dell'output. 








