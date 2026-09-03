# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_00:09:29_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-09-03 00:09:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-03 00:09:29 UTC

- **245,431** saved flights
- **74,163** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **245,431** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,955,906.5 tonnes** estimated CO2 emissions
- **171,356,898 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9844 |
| 2 | SkyWest Airlines | 8596 |
| 3 | EJA | 4734 |
| 4 | IndiGo | 4104 |
| 5 | American Airlines | 3942 |
| 6 | Southwest Airlines | 3678 |
| 7 | Delta Air Lines | 3122 |
| 8 | ENY | 2944 |
| 9 | LATAM Airlines | 2360 |
| 10 | AZU | 2281 |
| 11 | Vueling | 2100 |
| 12 | Lufthansa | 1964 |
| 13 | WIF | 1961 |
| 14 | LXJ | 1898 |
| 15 | easyJet | 1705 |
| 16 | Swiss International | 1654 |
| 17 | AXM | 1613 |
| 18 | EJU | 1580 |
| 19 | QLK | 1574 |
| 20 | United Airlines | 1546 |
| 21 | Alaska Airlines | 1467 |
| 22 | All Nippon Airways | 1446 |
| 23 | WMT | 1383 |
| 24 | GLO | 1370 |
| 25 | PGT | 1345 |
| 26 | VIV | 1344 |
| 27 | Air France | 1342 |
| 28 | Wizz Air | 1329 |
| 29 | AEE | 1211 |
| 30 | JetBlue | 1211 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 203405 |
| 2 | 🇪🇸 ES | 15751 |
| 3 | 🇧🇷 BR | 14312 |
| 4 | 🇦🇺 AU | 13955 |
| 5 | 🇨🇦 CA | 13668 |
| 6 | 🇮🇹 IT | 13450 |
| 7 | 🇮🇳 IN | 12797 |
| 8 | 🇩🇪 DE | 12102 |
| 9 | 🇬🇧 GB | 11565 |
| 10 | 🇨🇴 CO | 10657 |
| 11 | 🇫🇷 FR | 9904 |
| 12 | 🇯🇵 JP | 9759 |
| 13 | 🇹🇷 TR | 7299 |
| 14 | 🇬🇷 GR | 7234 |
| 15 | 🇲🇽 MX | 6769 |
| 16 | 🇨🇭 CH | 6593 |
| 17 | 🇳🇴 NO | 6088 |
| 18 | 🇹🇭 TH | 4429 |
| 19 | 🇲🇾 MY | 4324 |
| 20 | 🇿🇦 ZA | 4259 |
| 21 | 🇵🇱 PL | 4118 |
| 22 | 🇳🇿 NZ | 3364 |
| 23 | 🇵🇭 PH | 3357 |
| 24 | 🇬🇹 GT | 3075 |
| 25 | 🇰🇷 KR | 2876 |
| 26 | 🇭🇷 HR | 2825 |
| 27 | 🇲🇦 MA | 2479 |
| 28 | 🇲🇪 ME | 2296 |
| 29 | 🇳🇱 NL | 2220 |
| 30 | 🇮🇩 ID | 2137 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5057 |
| 2 | Denver International Airport |  | US | 3964 |
| 3 | Indira Gandhi International Airport |  | IN | 2986 |
| 4 | Tokyo International Airport |  | JP | 2910 |
| 5 | Guaymaral Airport |  | CO | 2718 |
| 6 | Harry Reid International Airport |  | US | 2614 |
| 7 | Zurich Airport |  | CH | 2577 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2496 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2443 |
| 10 | El Dorado International Airport |  | CO | 2428 |
| 11 | La Aurora Airport |  | GT | 2340 |
| 12 | Salt Lake City International Airport |  | US | 2177 |
| 13 | Chicago O'Hare International Airport |  | US | 2163 |
| 14 | Congonhas Airport |  | BR | 2100 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2027 |
| 16 | Frankfurt am Main International Airport |  | DE | 1935 |
| 17 | Capua Airport |  | IT | 1929 |
| 18 | Madrid Barajas International Airport |  | ES | 1927 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1844 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1804 |
| 21 | Malpensa International Airport |  | IT | 1757 |
| 22 | Charles de Gaulle International Airport |  | FR | 1727 |
| 23 | General Edward Lawrence Logan International Airport |  | US | 1725 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1721 |
| 25 | Ninoy Aquino International Airport |  | PH | 1634 |
| 26 | Macau International Airport |  | MO | 1632 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1588 |
| 28 | Charlotte/Douglas International Airport |  | US | 1565 |
| 29 | Kuala Lumpur International Airport |  | MY | 1558 |
| 30 | Barcelona International Airport |  | ES | 1552 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1490 |
| 32 | Viracopos International Airport |  | BR | 1457 |
| 33 | Seattle-Tacoma International Airport |  | US | 1443 |
| 34 | Don Mueang International Airport |  | TH | 1424 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1423 |
| 36 | Bengaluru International Airport |  | IN | 1416 |
| 37 | Calgary International Airport |  | CA | 1414 |
| 38 | Oslo Gardermoen Airport |  | NO | 1383 |
| 39 | Vancouver International Airport |  | CA | 1369 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1341 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 907 | 21m | 244 km | 3,819.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 638 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 624 | 24m | 225 km | 2,420.8 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 615 | 1h 6m | 770 km | 8,169.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 551 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 405 | 27m | 275 km | 1,919.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 387 | 1h 50m | 1,423 km | 9,497.6 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 376 | 44m | 555 km | 3,600.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 361 | 44m | 241 km | 1,499.5 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 348 | 21m | 250 km | 1,503.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 337 | 24m | 218 km | 1,269.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 328 | 1h 39m | 1,156 km | 6,543.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 325 | 22m | 55 km | 308.9 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 303 | 19m | 99 km | 519.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 300 | 27m | 215 km | 1,111.1 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 289 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 284 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 283 | 1h 14m | 961 km | 4,690.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 278 | 19m | 144 km | 691.5 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 265 | 1h 50m | 1,304 km | 5,961.8 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 252 | 28m | 152 km | 658.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DLH492 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Vancouver International Airport (CYVR) | 2026-09-02 12:11 UTC | 2026-09-03 00:09 UTC | 11h 57m |
| N535JM |  | Van Nuys Airport (KVNY) | Scottsdale Airport (KSDL) | 2026-09-02 23:04 UTC | 2026-09-03 00:02 UTC | 57m |
| TCF658 | TCF | Melbourne Orlando International Airport (KMLB) | Orlando Apopka Airport (KX04) | 2026-09-02 23:26 UTC | 2026-09-03 00:01 UTC | 34m |
| CAP2164 | CAP | Airlake Airport (KLVN) | Airlake Airport (KLVN) | 2026-09-02 23:22 UTC | 2026-09-03 00:01 UTC | 38m |
| N67CF |  | Logan-Cache Airport (KLGU) | Morgan County Airport (K42U) | 2026-09-02 23:13 UTC | 2026-09-03 00:01 UTC | 47m |
| N585AW |  | Montgomery-Gibbs Executive Airport (KMYF) | Montgomery-Gibbs Executive Airport (KMYF) | 2026-09-02 23:47 UTC | 2026-09-03 00:00 UTC | 13m |
| ADY421 | ADY | Cairo International Airport (HECA) | Das Island Airport (OMAS) | 2026-09-02 21:18 UTC | 2026-09-02 23:57 UTC | 2h 39m |
| N901WF |  | Chumchal Farms Airport (71TA) | Santa Barbara Municipal Airport (KSBA) | 2026-09-02 21:14 UTC | 2026-09-02 23:55 UTC | 2h 41m |
| CXK592 | CXK | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-09-02 23:00 UTC | 2026-09-02 23:55 UTC | 54m |
| N8292Q |  | Nenana Municipal Airport (PANN) | Fairbanks International Airport (PAFA) | 2026-09-02 23:35 UTC | 2026-09-02 23:52 UTC | 16m |
| N15SB |  | Kansas City/Lee's Summit Regional Airport (KLXT) | IN71 (IN71) | 2026-09-02 22:27 UTC | 2026-09-02 23:51 UTC | 1h 23m |
| N441JC |  | Norfolk Regional/Karl Stefan Memorial Field (KOFK) | Logansport/Cass County Airport (KGGP) | 2026-09-02 22:11 UTC | 2026-09-02 23:48 UTC | 1h 37m |
| RJA507 | Royal Jordanian | Queen Alia International Airport (OJAI) | Hulwan (HE15) | 2026-09-02 22:52 UTC | 2026-09-02 23:48 UTC | 56m |
| CFRT71 | CFR | Hemet-Ryan Airport (KHMT) | Hemet-Ryan Airport (KHMT) | 2026-09-02 23:08 UTC | 2026-09-02 23:45 UTC | 36m |
| DLH584 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Giza Embaba Airport (HEEM) | 2026-09-02 20:13 UTC | 2026-09-02 23:43 UTC | 3h 30m |
| N1653F |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-02 23:20 UTC | 2026-09-02 23:40 UTC | 19m |
| N156PH |  | Cleveland-Hopkins International Airport (KCLE) | Stickle Cattle Farms Airport (MO78) | 2026-09-02 22:26 UTC | 2026-09-02 23:40 UTC | 1h 13m |
| N77NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-09-02 23:05 UTC | 2026-09-02 23:36 UTC | 30m |
| N174EM |  | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-09-02 16:56 UTC | 2026-09-02 23:36 UTC | 6h 39m |
| QLK28D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-09-02 23:05 UTC | 2026-09-02 23:36 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
