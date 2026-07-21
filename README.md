# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--21_11:14:12_UTC-green)

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

**Latest saved flight:** 2026-07-21 11:14:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-21 11:14:12 UTC

- **143,242** saved flights
- **48,007** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **143,242** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,717,886.5 tonnes** estimated CO2 emissions
- **99,587,623 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5827 |
| 2 | SkyWest Airlines | 5236 |
| 3 | EJA | 2819 |
| 4 | IndiGo | 2610 |
| 5 | American Airlines | 2295 |
| 6 | Southwest Airlines | 2158 |
| 7 | ENY | 1777 |
| 8 | Delta Air Lines | 1696 |
| 9 | Lufthansa | 1439 |
| 10 | LATAM Airlines | 1320 |
| 11 | Vueling | 1232 |
| 12 | AZU | 1231 |
| 13 | WIF | 1224 |
| 14 | LXJ | 1099 |
| 15 | AXM | 1063 |
| 16 | Swiss International | 1021 |
| 17 | easyJet | 935 |
| 18 | All Nippon Airways | 920 |
| 19 | QLK | 905 |
| 20 | Alaska Airlines | 903 |
| 21 | EJU | 880 |
| 22 | VIV | 797 |
| 23 | CXK | 765 |
| 24 | AEE | 763 |
| 25 | Air France | 761 |
| 26 | JetBlue | 760 |
| 27 | MXY | 744 |
| 28 | United Airlines | 743 |
| 29 | Cathay Pacific | 738 |
| 30 | GLO | 731 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 123163 |
| 2 | 🇪🇸 ES | 9337 |
| 3 | 🇦🇺 AU | 8225 |
| 4 | 🇮🇳 IN | 8178 |
| 5 | 🇧🇷 BR | 8075 |
| 6 | 🇨🇦 CA | 7545 |
| 7 | 🇮🇹 IT | 7466 |
| 8 | 🇩🇪 DE | 7412 |
| 9 | 🇬🇧 GB | 6557 |
| 10 | 🇯🇵 JP | 6028 |
| 11 | 🇫🇷 FR | 5688 |
| 12 | 🇨🇴 CO | 4592 |
| 13 | 🇲🇽 MX | 4159 |
| 14 | 🇬🇷 GR | 4073 |
| 15 | 🇳🇴 NO | 3832 |
| 16 | 🇨🇭 CH | 3716 |
| 17 | 🇹🇷 TR | 3382 |
| 18 | 🇲🇾 MY | 2773 |
| 19 | 🇵🇱 PL | 2415 |
| 20 | 🇿🇦 ZA | 2338 |
| 21 | 🇳🇿 NZ | 2203 |
| 22 | 🇹🇭 TH | 2128 |
| 23 | 🇰🇷 KR | 2035 |
| 24 | 🇵🇭 PH | 1932 |
| 25 | 🇬🇹 GT | 1874 |
| 26 | 🇲🇦 MA | 1495 |
| 27 | 🇲🇪 ME | 1420 |
| 28 | 🇳🇱 NL | 1347 |
| 29 | 🇭🇷 HR | 1304 |
| 30 | 🇲🇴 MO | 1198 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2951 |
| 2 | Denver International Airport |  | US | 2400 |
| 3 | Tokyo International Airport |  | JP | 1940 |
| 4 | Indira Gandhi International Airport |  | IN | 1814 |
| 5 | Harry Reid International Airport |  | US | 1798 |
| 6 | Guaymaral Airport |  | CO | 1738 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1638 |
| 8 | Zurich Airport |  | CH | 1590 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1502 |
| 10 | La Aurora Airport |  | GT | 1450 |
| 11 | Frankfurt am Main International Airport |  | DE | 1388 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1354 |
| 13 | Chicago O'Hare International Airport |  | US | 1337 |
| 14 | Salt Lake City International Airport |  | US | 1282 |
| 15 | El Dorado International Airport |  | CO | 1267 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1257 |
| 17 | Macau International Airport |  | MO | 1198 |
| 18 | Capua Airport |  | IT | 1167 |
| 19 | Madrid Barajas International Airport |  | ES | 1149 |
| 20 | Congonhas Airport |  | BR | 1148 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1132 |
| 22 | Kuala Lumpur International Airport |  | MY | 1072 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1041 |
| 24 | Charlotte/Douglas International Airport |  | US | 1033 |
| 25 | Charles de Gaulle International Airport |  | FR | 1006 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1001 |
| 27 | Bengaluru International Airport |  | IN | 976 |
| 28 | Malpensa International Airport |  | IT | 923 |
| 29 | Ninoy Aquino International Airport |  | PH | 902 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 877 |
| 31 | Barcelona International Airport |  | ES | 873 |
| 32 | Daniel K Inouye International Airport |  | US | 871 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 851 |
| 34 | Tenerife Norte Airport |  | ES | 826 |
| 35 | Calgary International Airport |  | CA | 816 |
| 36 | Seattle-Tacoma International Airport |  | US | 814 |
| 37 | Viracopos International Airport |  | BR | 811 |
| 38 | Amsterdam Airport Schiphol |  | NL | 809 |
| 39 | Scottsdale Airport |  | US | 806 |
| 40 | Vitoria/Foronda Airport |  | ES | 787 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 732 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 521 | 21m | 244 km | 2,193.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 351 | 24m | 225 km | 1,361.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 346 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 340 | 1h 9m | 770 km | 4,516.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 260 | 26m | 275 km | 1,232.0 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 212 | 22m | 55 km | 201.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 193 | 26m | 215 km | 714.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 193 | 1h 46m | 1,423 km | 4,736.5 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 190 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 179 | 28m | 152 km | 467.8 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 178 | 20m | 250 km | 768.9 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 172 | 18m | 144 km | 427.8 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 168 | 44m | 452 km | 1,309.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 166 | 1h 16m | 961 km | 2,751.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 1m | 695 km | 1,977.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 163 | 1h 38m | 1,156 km | 3,251.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 163 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FHPBH | FHP | La Mole Airport (LFTZ) | Nice-Cote d'Azur Airport (LFMN) | 2026-07-21 10:57 UTC | 2026-07-21 11:14 UTC | 17m |
| CCDPP | CCD | Robledillo De Mohernando Airport (LERM) | Robledillo De Mohernando Airport (LERM) | 2026-07-21 09:33 UTC | 2026-07-21 11:03 UTC | 1h 29m |
| AUA592B | Austrian Airlines | Bari / Palese International Airport (LIBD) | Vienna International Airport (LOWW) | 2026-07-21 08:38 UTC | 2026-07-21 10:59 UTC | 2h 20m |
| FHBVL | FHB | Dax Seyresse Airport (LFBY) | Dax Seyresse Airport (LFBY) | 2026-07-21 10:48 UTC | 2026-07-21 10:53 UTC | 5m |
| TYW524P | TYW | Olbia / Costa Smeralda Airport (LIEO) | Zurich Airport (LSZH) | 2026-07-21 09:18 UTC | 2026-07-21 10:47 UTC | 1h 29m |
| EZY23ZC | easyJet | Glasgow International Airport (EGPF) | Faro Airport (LPFR) | 2026-07-21 07:43 UTC | 2026-07-21 10:33 UTC | 2h 50m |
| I2331 |  | Pratica Di Mare Airport (LIRE) | Vlora Internationa Airport (LAVL) | 2026-07-21 07:12 UTC | 2026-07-21 10:28 UTC | 3h 16m |
| LOG96LP | LOG | Edinburgh Airport (EGPH) | XPLO (XPLO) | 2026-07-21 09:46 UTC | 2026-07-21 10:19 UTC | 33m |
| LOT7PV | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Nowy Sącz-Łososina Dolna Airport  (EPNL) | 2026-07-21 09:17 UTC | 2026-07-21 10:18 UTC | 1h 1m |
| C10 |  | Linz Airport (LOWL) | Wels Airport (LOLW) | 2026-07-21 10:12 UTC | 2026-07-21 10:16 UTC | 4m |
| HFA851 | HFA | Haifa International Airport (LLHA) | Paphos International Airport (LCPH) | 2026-07-21 09:26 UTC | 2026-07-21 10:15 UTC | 48m |
| AFR65JY | Air France | Charles de Gaulle International Airport (LFPG) | Marseille Provence Airport (LFML) | 2026-07-21 09:16 UTC | 2026-07-21 10:15 UTC | 58m |
| IBB95FY | IBB | Tenerife Norte Airport (GCXO) | Santo Tome Del Puerto Airport (LETP) | 2026-07-21 07:49 UTC | 2026-07-21 10:14 UTC | 2h 25m |
| MDA2374 | MDA | Makung Airport (RCQC) | Taipei Songshan Airport (RCSS) | 2026-07-21 09:31 UTC | 2026-07-21 10:14 UTC | 42m |
| BEL5WE | Brussels Airlines | Brussels Airport (EBBR) | Linate Airport (LIML) | 2026-07-21 09:07 UTC | 2026-07-21 10:13 UTC | 1h 6m |
| ANE2328 | ANE | Palma De Mallorca Airport (LEPA) | Calaf-Sallavinera Airport (LECF) | 2026-07-21 09:33 UTC | 2026-07-21 10:13 UTC | 40m |
| CTV764 | CTV | Soekarno-Hatta International Airport (WIII) | Achmad Yani Airport (WARS) | 2026-07-21 09:38 UTC | 2026-07-21 10:13 UTC | 34m |
| EIN55G | Aer Lingus | Lyon Saint-Exupery Airport (LFLL) | Dublin Airport (EIDW) | 2026-07-21 08:22 UTC | 2026-07-21 10:13 UTC | 1h 50m |
| RYR8LD | Ryanair | Malaga Airport (LEMG) | Marseille Provence Airport (LFML) | 2026-07-21 08:48 UTC | 2026-07-21 10:13 UTC | 1h 25m |
| WZZ9SF | Wizz Air | M. R. Stefanik Airport (LZIB) | Kukes Airport (LAKU) | 2026-07-21 09:15 UTC | 2026-07-21 10:13 UTC | 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
