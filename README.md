# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_16:25:47_UTC-green)

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

**Latest saved flight:** 2026-09-19 16:25:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-19 16:25:47 UTC

- **263,545** saved flights
- **77,836** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **263,545** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,192,491.2 tonnes** estimated CO2 emissions
- **185,071,952 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10423 |
| 2 | SkyWest Airlines | 9162 |
| 3 | EJA | 5112 |
| 4 | IndiGo | 4435 |
| 5 | American Airlines | 4128 |
| 6 | Southwest Airlines | 3871 |
| 7 | Delta Air Lines | 3287 |
| 8 | ENY | 3106 |
| 9 | LATAM Airlines | 2539 |
| 10 | AZU | 2475 |
| 11 | Vueling | 2215 |
| 12 | WIF | 2128 |
| 13 | LXJ | 2065 |
| 14 | Lufthansa | 2033 |
| 15 | easyJet | 1781 |
| 16 | Swiss International | 1738 |
| 17 | QLK | 1701 |
| 18 | EJU | 1663 |
| 19 | AXM | 1660 |
| 20 | United Airlines | 1616 |
| 21 | Alaska Airlines | 1561 |
| 22 | All Nippon Airways | 1522 |
| 23 | PGT | 1482 |
| 24 | WMT | 1482 |
| 25 | GLO | 1470 |
| 26 | Air France | 1445 |
| 27 | VIV | 1439 |
| 28 | Wizz Air | 1430 |
| 29 | CXK | 1278 |
| 30 | TKR | 1275 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 218904 |
| 2 | 🇪🇸 ES | 16621 |
| 3 | 🇧🇷 BR | 15416 |
| 4 | 🇦🇺 AU | 15106 |
| 5 | 🇨🇦 CA | 14666 |
| 6 | 🇮🇹 IT | 14326 |
| 7 | 🇮🇳 IN | 14014 |
| 8 | 🇩🇪 DE | 12743 |
| 9 | 🇬🇧 GB | 12233 |
| 10 | 🇨🇴 CO | 11944 |
| 11 | 🇫🇷 FR | 10536 |
| 12 | 🇯🇵 JP | 10206 |
| 13 | 🇹🇷 TR | 7983 |
| 14 | 🇬🇷 GR | 7647 |
| 15 | 🇲🇽 MX | 7248 |
| 16 | 🇨🇭 CH | 7041 |
| 17 | 🇳🇴 NO | 6513 |
| 18 | 🇹🇭 TH | 4732 |
| 19 | 🇲🇾 MY | 4472 |
| 20 | 🇿🇦 ZA | 4442 |
| 21 | 🇵🇱 PL | 4348 |
| 22 | 🇳🇿 NZ | 3652 |
| 23 | 🇵🇭 PH | 3508 |
| 24 | 🇬🇹 GT | 3359 |
| 25 | 🇭🇷 HR | 3005 |
| 26 | 🇰🇷 KR | 2992 |
| 27 | 🇲🇦 MA | 2638 |
| 28 | 🇲🇪 ME | 2473 |
| 29 | 🇳🇱 NL | 2365 |
| 30 | 🇮🇩 ID | 2216 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5386 |
| 2 | Denver International Airport |  | US | 4261 |
| 3 | Indira Gandhi International Airport |  | IN | 3166 |
| 4 | Tokyo International Airport |  | JP | 3047 |
| 5 | Harry Reid International Airport |  | US | 2801 |
| 6 | El Dorado International Airport |  | CO | 2797 |
| 7 | Guaymaral Airport |  | CO | 2782 |
| 8 | Zurich Airport |  | CH | 2743 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2648 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2554 |
| 11 | La Aurora Airport |  | GT | 2553 |
| 12 | Salt Lake City International Airport |  | US | 2326 |
| 13 | Chicago O'Hare International Airport |  | US | 2266 |
| 14 | Congonhas Airport |  | BR | 2251 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2152 |
| 16 | Capua Airport |  | IT | 2058 |
| 17 | Madrid Barajas International Airport |  | ES | 2037 |
| 18 | Frankfurt am Main International Airport |  | DE | 2014 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1987 |
| 20 | Malpensa International Airport |  | IT | 1899 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1889 |
| 22 | Charles de Gaulle International Airport |  | FR | 1862 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1856 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1826 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1801 |
| 26 | Macau International Airport |  | MO | 1752 |
| 27 | Ninoy Aquino International Airport |  | PH | 1722 |
| 28 | Barcelona International Airport |  | ES | 1646 |
| 29 | Charlotte/Douglas International Airport |  | US | 1642 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1621 |
| 31 | Kuala Lumpur International Airport |  | MY | 1603 |
| 32 | Viracopos International Airport |  | BR | 1599 |
| 33 | Seattle-Tacoma International Airport |  | US | 1546 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1534 |
| 35 | Don Mueang International Airport |  | TH | 1502 |
| 36 | Calgary International Airport |  | CA | 1502 |
| 37 | Bengaluru International Airport |  | IN | 1498 |
| 38 | Oslo Gardermoen Airport |  | NO | 1485 |
| 39 | Vancouver International Airport |  | CA | 1474 |
| 40 | Antalya International Airport |  | TR | 1410 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1113 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 986 | 21m | 244 km | 4,151.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 723 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 662 | 1h 6m | 770 km | 8,794.2 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 657 | 24m | 225 km | 2,548.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 591 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 429 | 44m | 555 km | 4,107.9 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 425 | 27m | 275 km | 2,013.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 417 | 1h 50m | 1,423 km | 10,233.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 402 | 44m | 241 km | 1,669.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 376 | 24m | 218 km | 1,416.5 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 350 | 23m | 55 km | 332.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 333 | 1h 6m | 706 km | 4,054.3 t |
| 17 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 333 | 12m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 326 | 26m | 215 km | 1,207.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 326 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 307 | 19m | 144 km | 763.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 284 | 1h 50m | 1,304 km | 6,389.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 283 | 42m | 535 km | 2,613.7 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 282 | 28m | 152 km | 737.0 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N720CG |  | Lehigh Valley International Airport (KABE) | Lehigh Valley International Airport (KABE) | 2026-09-19 15:54 UTC | 2026-09-19 16:25 UTC | 31m |
| DEBEY | DEB | Koblenz-Winningen Airport (EDRK) | Bonn-Hangelar Airport (EDKB) | 2026-09-19 16:06 UTC | 2026-09-19 16:23 UTC | 17m |
| N884AD |  | Webster Field (ME91) | Nice-Cote d'Azur Airport (LFMN) | 2026-09-19 10:18 UTC | 2026-09-19 16:20 UTC | 6h 2m |
| N8417P |  | OI34 (OI34) | OI34 (OI34) | 2026-09-19 15:59 UTC | 2026-09-19 16:18 UTC | 19m |
| N716AT |  | Ralph Wien Memorial Airport (PAOT) | Bob Baker Memorial Airport (PAIK) | 2026-09-19 15:53 UTC | 2026-09-19 16:18 UTC | 24m |
| N851MH |  | Long Beach (Daugherty Field) Airport (KLGB) | Catalina Airport (KAVX) | 2026-09-19 15:59 UTC | 2026-09-19 16:12 UTC | 13m |
| OUA21 | OUA | Durant Regional/Eaker Field (KDUA) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-09-19 15:25 UTC | 2026-09-19 16:10 UTC | 44m |
| N657DA |  | Freedom Springs Ranch Airport (TA66) | San Antonio International Airport (KSAT) | 2026-09-19 15:47 UTC | 2026-09-19 16:03 UTC | 16m |
| N92DV |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-09-19 15:46 UTC | 2026-09-19 16:03 UTC | 17m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-09-19 15:40 UTC | 2026-09-19 16:03 UTC | 22m |
| JUMP13 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-09-19 15:45 UTC | 2026-09-19 16:00 UTC | 14m |
| N5765B |  | Reek Ranch Airport (ID63) | Reek Ranch Airport (ID63) | 2026-09-19 15:36 UTC | 2026-09-19 15:59 UTC | 23m |
| N3455S |  | Sullivan Regional Airport (KUUV) | Sullivan Regional Airport (KUUV) | 2026-09-19 15:35 UTC | 2026-09-19 15:59 UTC | 24m |
| HBZWE | HBZ | Reichenbach Air Base (LSGR) | Raron Airport (LSTA) | 2026-09-19 15:38 UTC | 2026-09-19 15:58 UTC | 19m |
| FGKDM | FGK | Lyon Corbas Airport (LFHJ) | Lyon Corbas Airport (LFHJ) | 2026-09-19 14:17 UTC | 2026-09-19 15:56 UTC | 1h 39m |
| N842EB |  | Sebastian Municipal Airport (KX26) | Sebastian Municipal Airport (KX26) | 2026-09-19 14:45 UTC | 2026-09-19 15:56 UTC | 1h 11m |
| CXK646 | CXK | 19OK (19OK) | Jones Memorial Airport (K3F7) | 2026-09-19 15:39 UTC | 2026-09-19 15:56 UTC | 16m |
| N68460 |  | Modesto City-County-Harry Sham Field (KMOD) | Sacramento Executive Airport (KSAC) | 2026-09-19 15:13 UTC | 2026-09-19 15:55 UTC | 41m |
| N52NG |  | North Las Vegas Airport (KVGT) | San Diego International Airport (KSAN) | 2026-09-19 14:48 UTC | 2026-09-19 15:53 UTC | 1h 5m |
| CXK333 | CXK | Flying L Airpark (6TX7) | Arlington Municipal Airport (KGKY) | 2026-09-19 15:46 UTC | 2026-09-19 15:52 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
