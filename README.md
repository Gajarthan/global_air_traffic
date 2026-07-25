# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_14:27:58_UTC-green)

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

**Latest saved flight:** 2026-07-25 14:27:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-25 14:27:58 UTC

- **150,041** saved flights
- **49,956** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **150,041** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,795,601.0 tonnes** estimated CO2 emissions
- **104,092,811 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6052 |
| 2 | SkyWest Airlines | 5480 |
| 3 | EJA | 2968 |
| 4 | IndiGo | 2683 |
| 5 | American Airlines | 2382 |
| 6 | Southwest Airlines | 2273 |
| 7 | ENY | 1864 |
| 8 | Delta Air Lines | 1764 |
| 9 | Lufthansa | 1470 |
| 10 | LATAM Airlines | 1380 |
| 11 | AZU | 1301 |
| 12 | WIF | 1276 |
| 13 | Vueling | 1265 |
| 14 | LXJ | 1154 |
| 15 | AXM | 1081 |
| 16 | Swiss International | 1058 |
| 17 | easyJet | 972 |
| 18 | All Nippon Airways | 952 |
| 19 | Alaska Airlines | 936 |
| 20 | QLK | 931 |
| 21 | EJU | 916 |
| 22 | VIV | 828 |
| 23 | CXK | 804 |
| 24 | AEE | 790 |
| 25 | MXY | 783 |
| 26 | Air France | 782 |
| 27 | JetBlue | 782 |
| 28 | Cathay Pacific | 781 |
| 29 | GLO | 776 |
| 30 | United Airlines | 772 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 129324 |
| 2 | 🇪🇸 ES | 9695 |
| 3 | 🇦🇺 AU | 8505 |
| 4 | 🇧🇷 BR | 8469 |
| 5 | 🇮🇳 IN | 8450 |
| 6 | 🇨🇦 CA | 8032 |
| 7 | 🇮🇹 IT | 7746 |
| 8 | 🇩🇪 DE | 7686 |
| 9 | 🇬🇧 GB | 6876 |
| 10 | 🇯🇵 JP | 6247 |
| 11 | 🇫🇷 FR | 5943 |
| 12 | 🇨🇴 CO | 5054 |
| 13 | 🇲🇽 MX | 4339 |
| 14 | 🇬🇷 GR | 4261 |
| 15 | 🇳🇴 NO | 3995 |
| 16 | 🇨🇭 CH | 3952 |
| 17 | 🇹🇷 TR | 3548 |
| 18 | 🇲🇾 MY | 2817 |
| 19 | 🇵🇱 PL | 2546 |
| 20 | 🇿🇦 ZA | 2446 |
| 21 | 🇳🇿 NZ | 2265 |
| 22 | 🇹🇭 TH | 2191 |
| 23 | 🇰🇷 KR | 2065 |
| 24 | 🇵🇭 PH | 2005 |
| 25 | 🇬🇹 GT | 1955 |
| 26 | 🇲🇦 MA | 1525 |
| 27 | 🇲🇪 ME | 1477 |
| 28 | 🇳🇱 NL | 1385 |
| 29 | 🇭🇷 HR | 1365 |
| 30 | 🇲🇴 MO | 1248 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3081 |
| 2 | Denver International Airport |  | US | 2515 |
| 3 | Tokyo International Airport |  | JP | 1993 |
| 4 | Indira Gandhi International Airport |  | IN | 1874 |
| 5 | Guaymaral Airport |  | CO | 1872 |
| 6 | Harry Reid International Airport |  | US | 1857 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1686 |
| 8 | Zurich Airport |  | CH | 1640 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1573 |
| 10 | La Aurora Airport |  | GT | 1513 |
| 11 | Frankfurt am Main International Airport |  | DE | 1417 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1405 |
| 13 | Chicago O'Hare International Airport |  | US | 1383 |
| 14 | Salt Lake City International Airport |  | US | 1348 |
| 15 | El Dorado International Airport |  | CO | 1344 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1286 |
| 17 | Macau International Airport |  | MO | 1248 |
| 18 | Congonhas Airport |  | BR | 1212 |
| 19 | Madrid Barajas International Airport |  | ES | 1195 |
| 20 | Capua Airport |  | IT | 1193 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1162 |
| 22 | Kuala Lumpur International Airport |  | MY | 1085 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1076 |
| 24 | Charlotte/Douglas International Airport |  | US | 1067 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1051 |
| 26 | Charles de Gaulle International Airport |  | FR | 1032 |
| 27 | Bengaluru International Airport |  | IN | 1007 |
| 28 | Malpensa International Airport |  | IT | 977 |
| 29 | Ninoy Aquino International Airport |  | PH | 939 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 912 |
| 31 | Barcelona International Airport |  | ES | 901 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 899 |
| 33 | Daniel K Inouye International Airport |  | US | 897 |
| 34 | Seattle-Tacoma International Airport |  | US | 861 |
| 35 | Tenerife Norte Airport |  | ES | 860 |
| 36 | Calgary International Airport |  | CA | 854 |
| 37 | Viracopos International Airport |  | BR | 851 |
| 38 | Scottsdale Airport |  | US | 851 |
| 39 | Amsterdam Airport Schiphol |  | NL | 832 |
| 40 | Oslo Gardermoen Airport |  | NO | 828 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 790 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 543 | 21m | 244 km | 2,286.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 364 | 24m | 225 km | 1,412.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 363 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 353 | 1h 9m | 770 km | 4,689.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 274 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 268 | 27m | 275 km | 1,269.9 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 224 | 22m | 55 km | 212.9 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 205 | 44m | 241 km | 851.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 201 | 1h 47m | 1,423 km | 4,932.9 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 197 | 20m | 99 km | 337.4 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 185 | 20m | 250 km | 799.1 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 183 | 27m | 152 km | 478.2 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 177 | 31m | 369 km | 1,126.6 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 177 | 1h 16m | 961 km | 2,933.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 177 | 18m | 144 km | 440.3 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 176 | 30m | 49 km | 148.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 175 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 173 | 44m | 452 km | 1,348.3 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 170 | 1h 1m | 695 km | 2,037.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 168 | 1h 39m | 1,156 km | 3,351.5 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 163 | 55m | 136 km | 382.1 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N737GK |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-07-25 13:58 UTC | 2026-07-25 14:27 UTC | 29m |
| N3504P |  | Dupage Airport (KDPA) | Lake In The Hills Airport (K3CK) | 2026-07-25 13:59 UTC | 2026-07-25 14:21 UTC | 21m |
| AEA68LW | AEA | Madrid Barajas International Airport (LEMD) | Vigo Airport (LEVX) | 2026-07-25 13:31 UTC | 2026-07-25 14:16 UTC | 44m |
| KAL2011 | Korean Air | Incheon International Airport (RKSI) | Macau International Airport (VMMC) | 2026-07-25 11:11 UTC | 2026-07-25 14:13 UTC | 3h 2m |
| DEAPR | DEA | Rendsburg-Schachtholm Airport (EDXR) | Lubeck Blankensee Airport (EDHL) | 2026-07-25 13:49 UTC | 2026-07-25 14:13 UTC | 23m |
| N20PN |  | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-07-25 13:52 UTC | 2026-07-25 14:12 UTC | 19m |
| OXF3571 | OXF | Falcon Field (KFFZ) | Rancho San Marcos Airport (74AZ) | 2026-07-25 12:41 UTC | 2026-07-25 14:10 UTC | 1h 29m |
| HBZVU | HBZ | Thun Airport (LSZW) | Reichenbach Air Base (LSGR) | 2026-07-25 13:57 UTC | 2026-07-25 14:08 UTC | 11m |
| 3AMAX |  | Nice-Cote d'Azur Airport (LFMN) | Nice-Cote d'Azur Airport (LFMN) | 2026-07-25 11:38 UTC | 2026-07-25 14:07 UTC | 2h 28m |
| LOG68GN | LOG | Glasgow International Airport (EGPF) | Glasgow International Airport (EGPF) | 2026-07-25 12:31 UTC | 2026-07-25 14:06 UTC | 1h 34m |
| RGA17 | RGA | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-07-25 13:57 UTC | 2026-07-25 14:04 UTC | 6m |
| N12441 |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-07-25 13:29 UTC | 2026-07-25 14:04 UTC | 34m |
| CXK118 | CXK | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-07-25 14:00 UTC | 2026-07-25 14:02 UTC | 2m |
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-07-25 12:55 UTC | 2026-07-25 14:01 UTC | 1h 6m |
| N257AK |  | Shannon Flight Strip (2GA8) | Pratermill Flight Park Airport (GA72) | 2026-07-25 13:36 UTC | 2026-07-25 14:00 UTC | 23m |
| N6053F |  | Morristown Municipal Airport (KMMU) | Lewis Landing Airport (NK79) | 2026-07-25 13:36 UTC | 2026-07-25 13:58 UTC | 22m |
| DLA8XN | DLA | Verona / Villafranca Airport (LIPX) | Frankfurt am Main International Airport (EDDF) | 2026-07-25 13:01 UTC | 2026-07-25 13:58 UTC | 56m |
| N98EG |  | Linden Airport (KLDJ) | Newark Liberty International Airport (KEWR) | 2026-07-25 13:47 UTC | 2026-07-25 13:58 UTC | 10m |
| N720LM |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-07-25 12:57 UTC | 2026-07-25 13:57 UTC | 59m |
| BOX545 | BOX | Brussels Airport (EBBR) | Frankfurt am Main International Airport (EDDF) | 2026-07-25 13:20 UTC | 2026-07-25 13:57 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
