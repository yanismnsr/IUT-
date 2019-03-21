create or replace function post(destinataire varchar, message text) returns boolean as
  $$
    declare
      dest name;
    begin
      select rolname into dest from pg_roles where rolcanlogin and rolname::varchar = destinataire;
      if not found then
        raise 'user % does not exist', destinataire;
        return false;
      end if;
      insert into m_envoyes (message, expediteir, destinataire) values (message, current_user, destinataire);
      insert into m_recus (message, expediteur, destinataire) values (message, current_user, destinataire);
      return true;
    end;
  $$ language plpgsql SECURITY DEFINER;


create or replace function get(out num int, out expe name, out quand timestamp, out mess text) returns setof record as
  $$
    declare
      curseur cursor for select numero, expediteur, date_envoie, message from m_recus where destinataire = current_user;
    begin
      open curseur;
      loop
        select numero, expediteur, date_envoie, message into num, expe, quand, mess from m_recus where destinataire = current_user;
        exit when not found;
        return next;
      end loop;
      close curseur;
      return;
    end;
  $$ language plpgsql security definer;
