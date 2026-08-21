# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_09:57:50_UTC-green)

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

**Latest saved flight:** 2026-08-21 09:57:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 09:57:50 UTC

- **221,645** saved flights
- **69,426** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **221,645** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,667,937.6 tonnes** estimated CO2 emissions
- **154,663,047 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8881 |
| 2 | SkyWest Airlines | 7891 |
| 3 | EJA | 4289 |
| 4 | IndiGo | 3756 |
| 5 | American Airlines | 3670 |
| 6 | Southwest Airlines | 3491 |
| 7 | Delta Air Lines | 2852 |
| 8 | ENY | 2724 |
| 9 | LATAM Airlines | 2103 |
| 10 | AZU | 2032 |
| 11 | Vueling | 1864 |
| 12 | Lufthansa | 1831 |
| 13 | WIF | 1772 |
| 14 | LXJ | 1746 |
| 15 | easyJet | 1531 |
| 16 | Swiss International | 1471 |
| 17 | AXM | 1462 |
| 18 | QLK | 1402 |
| 19 | United Airlines | 1390 |
| 20 | EJU | 1385 |
| 21 | Alaska Airlines | 1353 |
| 22 | All Nippon Airways | 1332 |
| 23 | GLO | 1211 |
| 24 | PGT | 1209 |
| 25 | VIV | 1206 |
| 26 | Air France | 1199 |
| 27 | WMT | 1175 |
| 28 | Wizz Air | 1130 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1107 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186304 |
| 2 | 🇪🇸 ES | 14201 |
| 3 | 🇧🇷 BR | 12790 |
| 4 | 🇦🇺 AU | 12635 |
| 5 | 🇨🇦 CA | 12245 |
| 6 | 🇮🇹 IT | 11790 |
| 7 | 🇮🇳 IN | 11713 |
| 8 | 🇩🇪 DE | 10923 |
| 9 | 🇬🇧 GB | 10381 |
| 10 | 🇨🇴 CO | 9102 |
| 11 | 🇯🇵 JP | 9034 |
| 12 | 🇫🇷 FR | 8817 |
| 13 | 🇬🇷 GR | 6469 |
| 14 | 🇹🇷 TR | 6389 |
| 15 | 🇲🇽 MX | 6157 |
| 16 | 🇨🇭 CH | 5845 |
| 17 | 🇳🇴 NO | 5510 |
| 18 | 🇲🇾 MY | 3872 |
| 19 | 🇿🇦 ZA | 3791 |
| 20 | 🇹🇭 TH | 3722 |
| 21 | 🇵🇱 PL | 3674 |
| 22 | 🇳🇿 NZ | 3089 |
| 23 | 🇵🇭 PH | 3015 |
| 24 | 🇬🇹 GT | 2793 |
| 25 | 🇰🇷 KR | 2649 |
| 26 | 🇭🇷 HR | 2462 |
| 27 | 🇲🇦 MA | 2224 |
| 28 | 🇳🇱 NL | 1968 |
| 29 | 🇲🇪 ME | 1958 |
| 30 | 🇮🇩 ID | 1895 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4649 |
| 2 | Denver International Airport |  | US | 3615 |
| 3 | Tokyo International Airport |  | JP | 2708 |
| 4 | Indira Gandhi International Airport |  | IN | 2691 |
| 5 | Guaymaral Airport |  | CO | 2606 |
| 6 | Harry Reid International Airport |  | US | 2443 |
| 7 | Zurich Airport |  | CH | 2293 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2276 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2248 |
| 10 | La Aurora Airport |  | GT | 2128 |
| 11 | El Dorado International Airport |  | CO | 2073 |
| 12 | Chicago O'Hare International Airport |  | US | 2024 |
| 13 | Salt Lake City International Airport |  | US | 1948 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1909 |
| 15 | Congonhas Airport |  | BR | 1869 |
| 16 | Frankfurt am Main International Airport |  | DE | 1798 |
| 17 | Madrid Barajas International Airport |  | ES | 1736 |
| 18 | Capua Airport |  | IT | 1692 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1661 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1630 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1625 |
| 22 | Macau International Airport |  | MO | 1586 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1570 |
| 24 | Malpensa International Airport |  | IT | 1552 |
| 25 | Charles de Gaulle International Airport |  | FR | 1524 |
| 26 | Charlotte/Douglas International Airport |  | US | 1471 |
| 27 | Ninoy Aquino International Airport |  | PH | 1435 |
| 28 | Kuala Lumpur International Airport |  | MY | 1414 |
| 29 | Barcelona International Airport |  | ES | 1360 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1346 |
| 31 | Bengaluru International Airport |  | IN | 1329 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1315 |
| 33 | Seattle-Tacoma International Airport |  | US | 1313 |
| 34 | Viracopos International Airport |  | BR | 1299 |
| 35 | Calgary International Airport |  | CA | 1256 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1235 |
| 37 | Oslo Gardermoen Airport |  | NO | 1233 |
| 38 | Vitoria/Foronda Airport |  | ES | 1229 |
| 39 | Don Mueang International Airport |  | TH | 1225 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1191 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1064 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 800 | 21m | 244 km | 3,368.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 552 | 1h 7m | 770 km | 7,332.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 499 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 499 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 373 | 27m | 275 km | 1,767.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 351 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 329 | 1h 50m | 1,423 km | 8,074.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 324 | 44m | 241 km | 1,345.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 293 | 21m | 250 km | 1,265.6 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 277 | 1h 38m | 1,156 km | 5,526.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 276 | 24m | 218 km | 1,039.8 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 273 | 19m | 99 km | 467.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 265 | 44m | 555 km | 2,537.5 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 261 | 1h 14m | 961 km | 4,326.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 252 | 19m | 144 km | 626.8 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 239 | 1h 49m | 1,304 km | 5,376.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CSZ662 | CSZ | Kansai International Airport (RJBB) | Guangzhou Baiyun International Airport (ZGGG) | 2026-08-21 06:39 UTC | 2026-08-21 09:57 UTC | 3h 18m |
| N314PH |  | 0NJ5 (0NJ5) | NJ47 (NJ47) | 2026-08-21 09:36 UTC | 2026-08-21 09:46 UTC | 10m |
| HBLZH | HBL | Friedrichshafen Airport (EDNY) | Mollis Airport (LSZM) | 2026-08-21 08:45 UTC | 2026-08-21 09:45 UTC | 59m |
| RMUS35 | RMU | Istres Le Tube/Istres Air Base (BA 125) Airport (LFMI) | Chateauneuf Sur Cher Airport (LFFU) | 2026-08-21 07:01 UTC | 2026-08-21 09:42 UTC | 2h 41m |
| GCLAP | GCL | Fowlmere Airfield (EGMA) | Fowlmere Airfield (EGMA) | 2026-08-21 09:21 UTC | 2026-08-21 09:35 UTC | 14m |
| 72250 |  | 6TE1 (6TE1) | Mid-Valley Dusters Inc Airport (43TX) | 2026-08-21 09:17 UTC | 2026-08-21 09:30 UTC | 13m |
| N604JA |  | Dallas Love Field (KDAL) | Draughon-Miller Central Texas Regional Airport (KTPL) | 2026-08-21 08:10 UTC | 2026-08-21 09:29 UTC | 1h 19m |
| 78741 |  | Ramenskoye Airport (UUBW) | Domodedovo International Airport (UUDD) | 2026-08-21 09:24 UTC | 2026-08-21 09:26 UTC | 1m |
| SVF664 | SVF | Borlange Airport (ESSD) | Stockholm-Bromma Airport (ESSB) | 2026-08-21 09:01 UTC | 2026-08-21 09:25 UTC | 23m |
| LSA211 | LSA | Ciampino Airport (LIRA) | Capua Airport (LIAU) | 2026-08-21 08:59 UTC | 2026-08-21 09:23 UTC | 23m |
| R20572 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-21 08:26 UTC | 2026-08-21 09:17 UTC | 50m |
| VJH387 | VJH | Václav Havel Airport (LKPR) | Mikonos Airport (LGMK) | 2026-08-21 06:42 UTC | 2026-08-21 09:15 UTC | 2h 33m |
| CPI211 | CPI | Ciampino Airport (LIRA) | Trieste / Ronchi Dei Legionari (LIPQ) | 2026-08-21 08:31 UTC | 2026-08-21 09:12 UTC | 41m |
| JL2325 |  | Osaka International Airport (RJOO) | Tajima Airport (RJBT) | 2026-08-21 08:47 UTC | 2026-08-21 09:09 UTC | 21m |
| HYP001 | HYP | Amsterdam Airport Schiphol (EHAM) | Ibiza Airport (LEIB) | 2026-08-21 06:55 UTC | 2026-08-21 09:08 UTC | 2h 12m |
| EAI91M | EAI | Leeds Bradford Airport (EGNM) | Dublin Airport (EIDW) | 2026-08-21 08:12 UTC | 2026-08-21 09:07 UTC | 54m |
| QLK1529 | QLK | Canberra International Airport (YSCB) | Melbourne International Airport (YMML) | 2026-08-21 08:08 UTC | 2026-08-21 09:06 UTC | 57m |
| RYR1512 | Ryanair | Perugia / San Egidio Airport (LIRZ) | Tortoli' / Arbatax Airport (LIET) | 2026-08-21 08:22 UTC | 2026-08-21 09:05 UTC | 43m |
| AWA475 | AWA | VGZR (VGZR) | Balurghat Airport (VEBG) | 2026-08-21 08:29 UTC | 2026-08-21 09:04 UTC | 35m |
| NOZ2FH | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Sørkjosen Airport (ENSR) | 2026-08-21 07:30 UTC | 2026-08-21 09:03 UTC | 1h 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
