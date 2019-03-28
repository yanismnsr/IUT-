create or replace function post (destinataire varchar, message text) returns boolean as
  $$
    declare
      dest varchar;
    begin
      select rolname into dest from pg_roles where rolcanlogin and rolname = destinataire;
      if not found then
        raise notice 'destinataire "%" introuvable', destinataire;
        return false;
      else
        insert into m_envoyes(message, expediteur, destinataire) values (message, session_user, dest);
        insert into m_recus(message, expediteur, destinataire) values (message, session_user, dest);
        return true;
      end if;
    end;
  $$ language plpgsql SECURITY DEFINER;



create or replace function get (out num int, out expe name, out quand timestamp, out mess text) returns setof record as
  $$
    declare
      mail cursor for
      select numero, expediteur, date_envoie, '<-' || message from m_recus where destinataire = session_user
      union
      select numero, destinataire, date_envoie, '->' || message from m_envoyes where expediteur = session_user order by date_envoie;
    begin
      open mail;
      loop
        fetch mail into num, expe, quand, mess;
        exit when not found;
        return next;
      end loop;
      close mail;
      return;
    end;
  $$ language plpgsql SECURITY DEFINER;


create or replace function l(out base varchar, out owner varchar, out privileges text) returns setof record as
  $$
    declare
      based cursor for
        select datname, pg_catalog.pg_get_userbyid(datdba), datacl from pg_database;
    begin
      open based;
      loop
        fetch based into base, owner, privileges ;
        exit when not found;
        return next;
      end loop;
      close based;
      return;
    end;
  $$ language plpgsql;


create or replace function l2(out base varchar, out owner varchar, out privileges text) returns setof record as
  $$
    select datname::varchar, pg_catalog.pg_get_userbyid(datdba)::varchar, datacl::text from pg_database;
  $$ language sql;
