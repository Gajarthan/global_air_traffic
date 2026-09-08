# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--08_10:41:52_UTC-green)

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

**Latest saved flight:** 2026-09-08 10:41:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-08 10:41:52 UTC

- **251,351** saved flights
- **75,382** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **251,351** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,026,864.2 tonnes** estimated CO2 emissions
- **175,470,391 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10061 |
| 2 | SkyWest Airlines | 8786 |
| 3 | EJA | 4857 |
| 4 | IndiGo | 4211 |
| 5 | American Airlines | 4018 |
| 6 | Southwest Airlines | 3723 |
| 7 | Delta Air Lines | 3182 |
| 8 | ENY | 3001 |
| 9 | LATAM Airlines | 2419 |
| 10 | AZU | 2335 |
| 11 | Vueling | 2143 |
| 12 | WIF | 2016 |
| 13 | Lufthansa | 1989 |
| 14 | LXJ | 1962 |
| 15 | easyJet | 1729 |
| 16 | Swiss International | 1688 |
| 17 | AXM | 1629 |
| 18 | QLK | 1619 |
| 19 | EJU | 1613 |
| 20 | United Airlines | 1571 |
| 21 | Alaska Airlines | 1501 |
| 22 | All Nippon Airways | 1474 |
| 23 | WMT | 1426 |
| 24 | GLO | 1395 |
| 25 | PGT | 1381 |
| 26 | VIV | 1376 |
| 27 | Air France | 1370 |
| 28 | Wizz Air | 1370 |
| 29 | AEE | 1230 |
| 30 | JetBlue | 1230 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 208449 |
| 2 | 🇪🇸 ES | 16065 |
| 3 | 🇧🇷 BR | 14645 |
| 4 | 🇦🇺 AU | 14311 |
| 5 | 🇨🇦 CA | 13943 |
| 6 | 🇮🇹 IT | 13769 |
| 7 | 🇮🇳 IN | 13144 |
| 8 | 🇩🇪 DE | 12346 |
| 9 | 🇬🇧 GB | 11783 |
| 10 | 🇨🇴 CO | 11064 |
| 11 | 🇫🇷 FR | 10112 |
| 12 | 🇯🇵 JP | 9906 |
| 13 | 🇹🇷 TR | 7513 |
| 14 | 🇬🇷 GR | 7384 |
| 15 | 🇲🇽 MX | 6941 |
| 16 | 🇨🇭 CH | 6773 |
| 17 | 🇳🇴 NO | 6230 |
| 18 | 🇹🇭 TH | 4533 |
| 19 | 🇲🇾 MY | 4379 |
| 20 | 🇿🇦 ZA | 4317 |
| 21 | 🇵🇱 PL | 4194 |
| 22 | 🇳🇿 NZ | 3432 |
| 23 | 🇵🇭 PH | 3411 |
| 24 | 🇬🇹 GT | 3137 |
| 25 | 🇰🇷 KR | 2907 |
| 26 | 🇭🇷 HR | 2890 |
| 27 | 🇲🇦 MA | 2537 |
| 28 | 🇲🇪 ME | 2366 |
| 29 | 🇳🇱 NL | 2267 |
| 30 | 🇮🇩 ID | 2149 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5189 |
| 2 | Denver International Airport |  | US | 4073 |
| 3 | Indira Gandhi International Airport |  | IN | 3056 |
| 4 | Tokyo International Airport |  | JP | 2955 |
| 5 | Guaymaral Airport |  | CO | 2740 |
| 6 | Harry Reid International Airport |  | US | 2672 |
| 7 | Zurich Airport |  | CH | 2631 |
| 8 | El Dorado International Airport |  | CO | 2552 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2550 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2486 |
| 11 | La Aurora Airport |  | GT | 2392 |
| 12 | Salt Lake City International Airport |  | US | 2225 |
| 13 | Chicago O'Hare International Airport |  | US | 2191 |
| 14 | Congonhas Airport |  | BR | 2150 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2070 |
| 16 | Capua Airport |  | IT | 1985 |
| 17 | Madrid Barajas International Airport |  | ES | 1977 |
| 18 | Frankfurt am Main International Airport |  | DE | 1958 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1883 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1829 |
| 21 | Malpensa International Airport |  | IT | 1807 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1768 |
| 23 | Charles de Gaulle International Airport |  | FR | 1761 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1748 |
| 25 | Ninoy Aquino International Airport |  | PH | 1665 |
| 26 | Enrique Olaya Herrera Airport |  | CO | 1660 |
| 27 | Macau International Airport |  | MO | 1652 |
| 28 | Barcelona International Airport |  | ES | 1588 |
| 29 | Charlotte/Douglas International Airport |  | US | 1586 |
| 30 | Kuala Lumpur International Airport |  | MY | 1577 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1540 |
| 32 | Viracopos International Airport |  | BR | 1500 |
| 33 | Seattle-Tacoma International Airport |  | US | 1484 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1459 |
| 35 | Don Mueang International Airport |  | TH | 1452 |
| 36 | Calgary International Airport |  | CA | 1445 |
| 37 | Bengaluru International Airport |  | IN | 1436 |
| 38 | Oslo Gardermoen Airport |  | NO | 1415 |
| 39 | Vancouver International Airport |  | CA | 1402 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1361 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 933 | 21m | 244 km | 3,928.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 665 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 635 | 24m | 225 km | 2,463.5 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 632 | 1h 6m | 770 km | 8,395.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 564 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 413 | 27m | 275 km | 1,957.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 402 | 1h 50m | 1,423 km | 9,865.7 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 395 | 44m | 555 km | 3,782.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 374 | 44m | 241 km | 1,553.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 352 | 21m | 250 km | 1,520.4 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 350 | 24m | 218 km | 1,318.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 335 | 23m | 55 km | 318.4 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 311 | 26m | 215 km | 1,151.8 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 293 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 289 | 19m | 144 km | 718.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 272 | 1h 50m | 1,304 km | 6,119.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 260 | 41m | 535 km | 2,401.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 257 | 28m | 152 km | 671.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FCK2FT | FCK | Sion Airport (LSGS) | Raron Airport (LSTA) | 2026-09-08 10:11 UTC | 2026-09-08 10:41 UTC | 30m |
| TJD402 | TJD | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | Capua Airport (LIAU) | 2026-09-08 09:42 UTC | 2026-09-08 10:37 UTC | 55m |
| LIFTR02 | LIF | Wunstorf Airport (ETNW) | Siegerland Airport (EDGS) | 2026-09-08 09:47 UTC | 2026-09-08 10:35 UTC | 48m |
| UAE9832 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-09-08 03:19 UTC | 2026-09-08 10:22 UTC | 7h 3m |
| IGO172 | IndiGo | Bengaluru International Airport (VOBL) | Behala Airport (VEBA) | 2026-09-08 08:14 UTC | 2026-09-08 10:17 UTC | 2h 2m |
| AIC6BS | Air India | Juhu Aerodrome (VAJJ) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-08 07:42 UTC | 2026-09-08 10:12 UTC | 2h 30m |
| HBJIM | HBJ | Zurich Airport (LSZH) | Friedrichshafen Airport (EDNY) | 2026-09-08 09:38 UTC | 2026-09-08 09:57 UTC | 19m |
| SFJ85 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-09-08 08:47 UTC | 2026-09-08 09:54 UTC | 1h 7m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-09-08 09:13 UTC | 2026-09-08 09:53 UTC | 39m |
| IGO082 | IndiGo | King Fahd International Airport (OEDF) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-08 06:42 UTC | 2026-09-08 09:52 UTC | 3h 10m |
| RYR12HZ | Ryanair | Luqa Airport (LMML) | Tomaszów Mazowiecki Military Air Base (EPTM) | 2026-09-08 07:13 UTC | 2026-09-08 09:50 UTC | 2h 36m |
| RYR17MN | Ryanair | Malaga Airport (LEMG) | Krnov Airport (LKKR) | 2026-09-08 06:28 UTC | 2026-09-08 09:50 UTC | 3h 21m |
| DLH5AL | Lufthansa | Dresden Airport (EDDC) | Frankfurt am Main International Airport (EDDF) | 2026-09-08 09:01 UTC | 2026-09-08 09:47 UTC | 46m |
| XUM2597 | XUM | Gimpo International Airport (RKSS) | Sacheon Air Base (RKPS) | 2026-09-08 09:01 UTC | 2026-09-08 09:47 UTC | 46m |
| SIO401 | SIO | Rimini / Miramare - Federico Fellini International Airport (LIPR) | Samedan Airport (LSZS) | 2026-09-08 09:11 UTC | 2026-09-08 09:46 UTC | 35m |
| AFR32GL | Air France | Charles de Gaulle International Airport (LFPG) | Budapest Ferenc Liszt International Airport (LHBP) | 2026-09-08 08:01 UTC | 2026-09-08 09:45 UTC | 1h 43m |
| BGA183J | BGA | Nantes Atlantique Airport (LFRS) | Hamburg-Finkenwerder Airport (EDHI) | 2026-09-08 08:04 UTC | 2026-09-08 09:44 UTC | 1h 39m |
| RYR70ED | Ryanair | Alghero / Fertilia Airport (LIEA) | Malpensa International Airport (LIMC) | 2026-09-08 08:43 UTC | 2026-09-08 09:43 UTC | 59m |
| UPS474 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Montréal (Mirabel) Airport (CYMX) | 2026-09-08 08:01 UTC | 2026-09-08 09:41 UTC | 1h 40m |
| PSVTS | PSV | Nascimento I Airport (SDNI) | Ubatuba Airport (SDUB) | 2026-09-08 09:16 UTC | 2026-09-08 09:41 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
